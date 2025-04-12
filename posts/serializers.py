from rest_framework import serializers
from .models import Post, Comment
from profiles.serializers import UserProfileSerializer

class PostSerializer(serializers.ModelSerializer):
    author = UserProfileSerializer(read_only=True)
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at']
        read_only_fields = ['author', 'created_at', 'updated_at']

class CommentSerializer(serializers.ModelSerializer):
    author = UserProfileSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'content', 'post', 'author', 'created_at', 'updated_at']
        read_only_fields = ['author', 'created_at', 'updated_at'] 