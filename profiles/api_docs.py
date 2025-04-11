from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# User Profile Schemas
user_profile_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID único del perfil'),
        'user': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                'username': openapi.Schema(type=openapi.TYPE_STRING),
                'email': openapi.Schema(type=openapi.TYPE_STRING),
                'first_name': openapi.Schema(type=openapi.TYPE_STRING),
                'last_name': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
        'avatar': openapi.Schema(type=openapi.TYPE_STRING, format='uri'),
        'bio': openapi.Schema(type=openapi.TYPE_STRING),
        'karma': openapi.Schema(type=openapi.TYPE_INTEGER),
        'is_online': openapi.Schema(type=openapi.TYPE_BOOLEAN),
        'last_active': openapi.Schema(type=openapi.TYPE_STRING, format='date-time'),
        'created_at': openapi.Schema(type=openapi.TYPE_STRING, format='date-time'),
        'updated_at': openapi.Schema(type=openapi.TYPE_STRING, format='date-time'),
    }
)

# API Documentation Decorators
list_profiles = swagger_auto_schema(
    operation_description="Lista todos los perfiles de usuario",
    responses={
        200: openapi.Response(
            description="Lista de perfiles de usuario",
            schema=openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=user_profile_schema
            )
        )
    },
    security=[{'Bearer': []}]
)

get_profile = swagger_auto_schema(
    operation_description="Obtiene el perfil de un usuario específico",
    responses={
        200: openapi.Response(
            description="Perfil de usuario",
            schema=user_profile_schema
        ),
        404: "Perfil no encontrado"
    },
    security=[{'Bearer': []}]
)

update_profile = swagger_auto_schema(
    operation_description="Actualiza el perfil de un usuario",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'avatar': openapi.Schema(type=openapi.TYPE_STRING, format='binary'),
            'bio': openapi.Schema(type=openapi.TYPE_STRING),
        }
    ),
    responses={
        200: openapi.Response(
            description="Perfil actualizado",
            schema=user_profile_schema
        ),
        400: "Datos inválidos",
        404: "Perfil no encontrado"
    },
    security=[{'Bearer': []}]
) 