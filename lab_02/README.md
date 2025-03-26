# 🚀 Proyecto HTML, CSS y JavaScript con Docker

Este proyecto es una estructura simple de una página web utilizando HTML, CSS y JavaScript.

## 📂 Estructura del Proyecto

El proyecto está compuesto por los siguientes archivos:

- 📝 **index.html**: Archivo principal que contiene la estructura de la página.
- 🎨 **css/lab01.css**: Archivo de estilos externos para mejorar la apariencia.
- ⚙️ **js/lab01.js**: Archivo de JavaScript para estilos adicionales.
- 🐳 **Dockerfile**: Archivo de configuración para desplegar el proyecto con Docker y Nginx.

## 📖 Descripción de los Archivos

### 🏗️ index.html

- Define una página básica con texto estilizado.
- Usa clases y un `id` para aplicar diferentes estilos.
- Incluye estilos internos en la etiqueta `<style>`.
- Hace referencia a `css/lab01.css` para estilos adicionales.
- Enlaza `js/lab01.js` para mejorar la apariencia con JavaScript.

### 🎨 css/lab01.css

- 🏞️ Define un fondo claro para la página.
- 🎭 Aplica estilos a elementos con clases y `id`.
- ✨ Mejora la apariencia del texto con colores y fuentes adecuadas.

### ⚙️ js/lab01.js

- Aplica estilos dinámicos a elementos con JavaScript.
- Ejemplo de código incluido:
  ```javascript
  let p = document.getElementById("JS");
  p.style.color = "blue";
  p.style.fontWeight = "bold";
  ```

### 🐳 Dockerfile

Este archivo permite desplegar el proyecto utilizando Docker y el servidor Nginx.

```dockerfile
FROM nginx:alpine
COPY . /usr/share/nginx/html
EXPOSE 8098
CMD ["nginx", "-g", "daemon off;"]
```

## 🔧 Instalación y Uso

1. 🐳 Para ejecutar con Docker:
   ```sh
   docker build -t lab02_test .
   docker run -p 8098:80 lab02_test
   ```
2. Abre en tu navegador:
👉 [http://localhost:8098](http://localhost:8098)
---
## ✍️ Autor

Desarrollado por Carla Fernanda Ropa Calizaya.

