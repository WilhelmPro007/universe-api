# Universe API

API para una aplicación similar a Reddit, desarrollada con Django y Django REST Framework.

## Índice
- [Requisitos](#requisitos)
- [Instalación](#instalación)
  - [Con entorno virtual (recomendado)](#con-entorno-virtual-recomendado)
  - [Sin entorno virtual](#sin-entorno-virtual)
- [Configuración](#configuración)
- [Ejecución](#ejecución)
- [Documentación de la API](#documentación-de-la-api)
  - [Autenticación](#autenticación)
  - [Endpoints](#endpoints)
- [Pruebas](#pruebas)

## Requisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git

## Instalación

### Con entorno virtual (recomendado)

1. Clona el repositorio:
```bash
git clone https://github.com/tu-usuario/universe-api.git
cd universe-api
```

2. Crea y activa el entorno virtual:
```bash
# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual
# En Windows
venv\Scripts\activate
# En Linux/Mac
source venv/bin/activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

### Sin entorno virtual

1. Clona el repositorio:
```bash
git clone https://github.com/tu-usuario/universe-api.git
cd universe-api
```

2. Instala las dependencias directamente:
```bash
pip install -r requirements.txt
```

> **Nota**: Se recomienda usar un entorno virtual para evitar conflictos con otras dependencias de Python en tu sistema.

## Configuración

1. Realiza las migraciones de la base de datos:
```bash
python manage.py migrate
```

2. Crea un superusuario (opcional):
```bash
python manage.py createsuperuser
```

## Ejecución

1. Inicia el servidor de desarrollo:
```bash
python manage.py runserver
```

2. Accede a la documentación de la API en:
- Swagger UI: http://127.0.0.1:8000/swagger/
- ReDoc: http://127.0.0.1:8000/redoc/

## Documentación de la API

### Autenticación

La API utiliza JWT (JSON Web Tokens) para la autenticación. Para obtener un token:

1. Ve a http://127.0.0.1:8000/swagger/
2. Busca el endpoint `/api/v1/auth/token/`
3. Haz clic en "Try it out"
4. Ingresa tus credenciales:
```json
{
  "username": "tu_usuario",
  "password": "tu_contraseña"
}
```
5. Haz clic en "Execute"
6. Copia el token de acceso (campo "access" en la respuesta)
7. Haz clic en el botón "Authorize" en la parte superior
8. Ingresa el token con el formato: `Bearer tu_token`
9. Haz clic en "Authorize"

### Endpoints

#### Usuarios
- `GET /api/v1/users/` - Lista todos los perfiles de usuario
- `GET /api/v1/users/{username}/` - Obtiene el perfil de un usuario específico
- `PATCH /api/v1/users/{username}/update_profile/` - Actualiza el perfil de un usuario

#### Chats
- `GET /api/v1/chats/` - Lista todas las conversaciones del usuario
- `POST /api/v1/chats/` - Crea una nueva conversación
- `GET /api/v1/chats/{id}/` - Obtiene los detalles de una conversación
- `POST /api/v1/chats/{id}/mark_read/` - Marca los mensajes como leídos

#### Mensajes
- `GET /api/v1/messages/` - Lista todos los mensajes
- `POST /api/v1/messages/` - Crea un nuevo mensaje

## Pruebas

Para probar la API usando Swagger UI:

1. Inicia el servidor:
```bash
python manage.py runserver
```

2. Abre http://127.0.0.1:8000/swagger/ en tu navegador

3. Obtén un token de acceso:
   - Busca el endpoint `/api/v1/auth/token/`
   - Haz clic en "Try it out"
   - Ingresa tus credenciales
   - Haz clic en "Execute"
   - Copia el token de acceso

4. Autoriza las peticiones:
   - Haz clic en "Authorize"
   - Ingresa `Bearer tu_token`
   - Haz clic en "Authorize"

5. Prueba los endpoints:
   - Expande cualquier endpoint que quieras probar
   - Haz clic en "Try it out"
   - Completa los parámetros necesarios
   - Haz clic en "Execute"