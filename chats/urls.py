from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'chats', views.ChatViewSet, basename='chat')
router.register(r'messages', views.MessageViewSet, basename='message')

urlpatterns = [
    path('', include(router.urls)),
    # Los endpoints se implementarán usando los decoradores de Swagger
    # path('api/v1/chats/', views.ChatViewSet.as_view({'get': 'list', 'post': 'create'}), name='chat-list'),
    # path('api/v1/chats/<int:chat_id>/', views.ChatViewSet.as_view({'get': 'retrieve'}), name='chat-detail'),
    # path('api/v1/chats/<int:chat_id>/messages/', views.MessageViewSet.as_view({'get': 'list', 'post': 'create'}), name='message-list'),
    # path('api/v1/chats/<int:chat_id>/read/', views.ChatViewSet.as_view({'post': 'mark_read'}), name='chat-read'),
] 