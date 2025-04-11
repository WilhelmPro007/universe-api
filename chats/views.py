from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer, ChatCreateSerializer
from . import api_docs

# Create your views here.

class ChatViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar conversaciones entre usuarios.
    """
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Chat.objects.none()
        return Chat.objects.filter(participants=self.request.user)

    @api_docs.list_chats
    def list(self, request):
        """
        Lista todas las conversaciones del usuario autenticado.
        """
        chats = self.get_queryset()
        serializer = self.get_serializer(chats, many=True)
        return Response(serializer.data)

    @api_docs.create_chat
    def create(self, request):
        """
        Crea una nueva conversación.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            chat = serializer.save()
            chat.participants.add(request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_docs.get_chat
    def retrieve(self, request, pk=None):
        """
        Obtiene los detalles de una conversación específica.
        """
        try:
            chat = self.get_queryset().get(pk=pk)
            serializer = self.get_serializer(chat)
            return Response(serializer.data)
        except Chat.DoesNotExist:
            return Response(
                {"error": "Conversación no encontrada"},
                status=status.HTTP_404_NOT_FOUND
            )

    @api_docs.mark_chat_read
    @action(detail=True, methods=['post'])
    def mark_read(self, request, pk=None):
        """
        Marca todos los mensajes de una conversación como leídos.
        """
        try:
            chat = self.get_queryset().get(pk=pk)
            chat.messages.filter(is_read=False).update(is_read=True)
            return Response({"status": "mensajes marcados como leídos"})
        except Chat.DoesNotExist:
            return Response(
                {"error": "Conversación no encontrada"},
                status=status.HTTP_404_NOT_FOUND
            )

class MessageViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar mensajes dentro de las conversaciones.
    """
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Message.objects.none()
        return Message.objects.filter(chat__participants=self.request.user)

    @api_docs.list_messages
    def list(self, request):
        """
        Lista todos los mensajes de las conversaciones del usuario.
        """
        messages = self.get_queryset()
        serializer = self.get_serializer(messages, many=True)
        return Response(serializer.data)

    @api_docs.create_message
    def create(self, request):
        """
        Crea un nuevo mensaje en una conversación.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            chat = serializer.validated_data['chat']
            if request.user not in chat.participants.all():
                return Response(
                    {"error": "No tienes permiso para enviar mensajes en esta conversación"},
                    status=status.HTTP_403_FORBIDDEN
                )
            serializer.save(sender=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
