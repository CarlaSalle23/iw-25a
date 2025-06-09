# 📘 Implementación de JWT en Django Rest Framework

Este proyecto es un ejemplo básico de una API con Django Rest Framework (DRF) que usa **autenticación JWT** para proteger rutas de tipo CRUD. El modelo base es un `Silabo` que representa la información académica de un curso.

## ⚙️ Requisitos

- Python 3.8+
- Django 4.x
- djangorestframework
- djangorestframework-simplejwt

## 🔧 Instalación

```bash
pip install django djangorestframework djangorestframework-simplejwt
```

## 🛠 Configuración en `settings.py`

Agrega a `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework_simplejwt',
]
```

Agrega esta configuración:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```

## 🔐 URLs para autenticación JWT

```python
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

## 🧪 Endpoints para JWT

### Obtener token

`POST /api/token/`

```json
{
  "username": "admin",
  "password": "admin123"
}
```

### Refrescar token

`POST /api/token/refresh/`

```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJh..."
}
```

## 📚 Modelo de ejemplo

```python
class Silabo(models.Model):
    curso = models.CharField(max_length=100)
    docente = models.CharField(max_length=100)
    semestre = models.CharField(max_length=10)
    contenido = models.TextField()
```

## 🧰 CRUD protegido con JWT

```http
Authorization: Bearer <ACCESS_TOKEN>
```

## 📦 Prueba con herramientas como Postman o curl

```bash
python manage.py createsuperuser
```

## ✅ Resultado

Sistema funcional con:
- CRUD protegido por JWT
- Login, refresh y uso de access token
- Seguridad robusta para APIs REST