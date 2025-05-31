# 📚 API de Sílabos - Centro Educativo

Este proyecto es una API REST construida con Django y Django REST Framework, diseñada para gestionar sílabos académicos de un centro educativo.

## 🚀 Requisitos

- Python 3.9+
- pip
- Virtualenv (opcional pero recomendado)
- Django 4.x
- djangorestframework

## 🔧 Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/tu_usuario/api-silabos.git
cd api-silabos
```

2. Crea y activa un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

4. Aplica las migraciones:
```bash
python manage.py migrate
```

5. Ejecuta el servidor de desarrollo:
```bash
python manage.py runserver
```

La API estará disponible en `http://127.0.0.1:8000/`.

## 🛠️ Endpoints principales

| Método | Endpoint               | Descripción                  |
|--------|------------------------|------------------------------|
| GET    | `/api/silabos/`        | Listar todos los sílabos     |
| POST   | `/api/silabos/`        | Crear nuevo sílabo           |
| GET    | `/api/silabos/<id>/`   | Obtener sílabo por ID        |
| PUT    | `/api/silabos/<id>/`   | Actualizar sílabo por ID     |
| DELETE | `/api/silabos/<id>/`   | Eliminar sílabo por ID       |

## 📦 Estructura del modelo

```python
class Silabo(models.Model):
    titulo = models.CharField(max_length=200)
    curso = models.CharField(max_length=100)
    docente = models.CharField(max_length=100)
    ciclo = models.CharField(max_length=20)
    competencias = models.TextField()
```

## 🧪 Pruebas con Postman

Puedes realizar pruebas con Postman usando JSON en el cuerpo de las solicitudes POST y PUT. Ejemplo:

```json
{
  "titulo": "Sílabo de Historia",
  "curso": "Historia Universal",
  "docente": "Lic. Soto",
  "ciclo": "2025-I",
  "competencias": "Comprensión crítica, análisis de fuentes históricas."
}
```

---

## ✍️ Autor

Desarrollado por Carla Ropa
