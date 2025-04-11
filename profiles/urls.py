from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserProfileViewSet, basename='user-profile')

urlpatterns = [
    path('', include(router.urls)),
    # Los endpoints se implementarán usando los decoradores de Swagger
    # path('api/v1/users/', views.UserProfileViewSet.as_view({'get': 'list'}), name='user-list'),
    # path('api/v1/users/<str:username>/', views.UserProfileViewSet.as_view({'get': 'retrieve'}), name='user-detail'),
    # path('api/v1/users/<str:username>/update/', views.UserProfileViewSet.as_view({'patch': 'update'}), name='user-update'),
] 