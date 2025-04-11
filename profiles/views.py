from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import UserProfile
from .serializers import UserProfileSerializer, UserProfileUpdateSerializer
from . import api_docs

# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'user__username'

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return UserProfile.objects.none()
        return UserProfile.objects.all()

    @api_docs.list_profiles
    def list(self, request):
        """
        Lista todos los perfiles de usuario.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @api_docs.get_profile
    def retrieve(self, request, user__username=None):
        """
        Obtiene el perfil de un usuario específico.
        """
        try:
            profile = UserProfile.objects.get(user__username=user__username)
            serializer = self.get_serializer(profile)
            return Response(serializer.data)
        except UserProfile.DoesNotExist:
            return Response(
                {"detail": "Perfil no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )

    @api_docs.update_profile
    @action(detail=True, methods=['patch'])
    def update_profile(self, request, user__username=None):
        """
        Actualiza el perfil de un usuario.
        """
        try:
            profile = UserProfile.objects.get(user__username=user__username)
            if request.user != profile.user:
                return Response(
                    {"detail": "No tienes permiso para actualizar este perfil"},
                    status=status.HTTP_403_FORBIDDEN
                )
            
            serializer = UserProfileUpdateSerializer(
                profile,
                data=request.data,
                partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(
                    UserProfileSerializer(profile).data,
                    status=status.HTTP_200_OK
                )
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        except UserProfile.DoesNotExist:
            return Response(
                {"detail": "Perfil no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
