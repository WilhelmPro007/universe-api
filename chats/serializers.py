from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Chat, Message
from profiles.serializers import UserSerializer

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    sender_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='sender',
        write_only=True
    )

    class Meta:
        model = Message
        fields = ('id', 'chat', 'sender', 'sender_id', 'content', 
                 'is_read', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

class ChatSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    last_message = serializers.SerializerMethodField()
    unread_count = serializers.SerializerMethodField()

    class Meta:
        model = Chat
        fields = ('id', 'participants', 'last_message', 'unread_count',
                 'is_active', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def get_last_message(self, obj):
        last_message = obj.messages.first()
        if last_message:
            return MessageSerializer(last_message).data
        return None

    def get_unread_count(self, obj):
        user = self.context['request'].user
        return obj.messages.filter(is_read=False).exclude(sender=user).count()

class ChatCreateSerializer(serializers.ModelSerializer):
    participant_ids = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True
    )

    class Meta:
        model = Chat
        fields = ('participant_ids',)

    def create(self, validated_data):
        participant_ids = validated_data.pop('participant_ids')
        chat = Chat.objects.create(**validated_data)
        chat.participants.set(participant_ids)
        return chat 