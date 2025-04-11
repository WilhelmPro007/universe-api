from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# Chat Schemas
chat_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_INTEGER),
        'participants': openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                    'username': openapi.Schema(type=openapi.TYPE_STRING),
                    'avatar': openapi.Schema(type=openapi.TYPE_STRING, format='uri'),
                }
            )
        ),
        'last_message': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                'content': openapi.Schema(type=openapi.TYPE_STRING),
                'sender': openapi.Schema(type=openapi.TYPE_OBJECT),
                'created_at': openapi.Schema(type=openapi.TYPE_STRING, format='date-time'),
            }
        ),
        'unread_count': openapi.Schema(type=openapi.TYPE_INTEGER),
        'is_active': openapi.Schema(type=openapi.TYPE_BOOLEAN),
        'created_at': openapi.Schema(type=openapi.TYPE_STRING, format='date-time'),
        'updated_at': openapi.Schema(type=openapi.TYPE_STRING, format='date-time'),
    }
)

message_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_INTEGER),
        'chat': openapi.Schema(type=openapi.TYPE_INTEGER),
        'sender': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                'username': openapi.Schema(type=openapi.TYPE_STRING),
                'avatar': openapi.Schema(type=openapi.TYPE_STRING, format='uri'),
            }
        ),
        'content': openapi.Schema(type=openapi.TYPE_STRING),
        'is_read': openapi.Schema(type=openapi.TYPE_BOOLEAN),
        'created_at': openapi.Schema(type=openapi.TYPE_STRING, format='date-time'),
        'updated_at': openapi.Schema(type=openapi.TYPE_STRING, format='date-time'),
    }
)

# API Documentation Decorators
list_chats = swagger_auto_schema(
    operation_description="Lista todas las conversaciones del usuario",
    responses={
        200: openapi.Response(
            description="Lista de conversaciones",
            schema=openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=chat_schema
            )
        )
    },
    security=[{'Bearer': []}]
)

create_chat = swagger_auto_schema(
    operation_description="Crea una nueva conversación",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'participant_ids': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(type=openapi.TYPE_INTEGER),
                description="Lista de IDs de usuarios participantes"
            ),
        }
    ),
    responses={
        201: openapi.Response(
            description="Conversación creada",
            schema=chat_schema
        ),
        400: "Datos inválidos"
    },
    security=[{'Bearer': []}]
)

get_chat = swagger_auto_schema(
    operation_description="Obtiene los detalles de una conversación",
    responses={
        200: openapi.Response(
            description="Detalles de la conversación",
            schema=chat_schema
        ),
        404: "Conversación no encontrada"
    },
    security=[{'Bearer': []}]
)

list_messages = swagger_auto_schema(
    operation_description="Lista los mensajes de una conversación",
    responses={
        200: openapi.Response(
            description="Lista de mensajes",
            schema=openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=message_schema
            )
        )
    },
    security=[{'Bearer': []}]
)

create_message = swagger_auto_schema(
    operation_description="Envía un nuevo mensaje en una conversación",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'content': openapi.Schema(type=openapi.TYPE_STRING),
        }
    ),
    responses={
        201: openapi.Response(
            description="Mensaje enviado",
            schema=message_schema
        ),
        400: "Datos inválidos",
        404: "Conversación no encontrada"
    },
    security=[{'Bearer': []}]
)

mark_chat_read = swagger_auto_schema(
    operation_description="Marca todos los mensajes de una conversación como leídos",
    responses={
        200: "Mensajes marcados como leídos",
        404: "Conversación no encontrada"
    },
    security=[{'Bearer': []}]
) 