# TuPrimeraPagina - Blog con Django

Este es un proyecto de blog simple creado con Django como parte de mi aprendizaje.

## Funcionalidades

- Creación de Posts, Autores y Categorías
- Búsqueda de Posts por título
- Interfaz administrativa

## Cómo probar el proyecto

1. Clonar el repositorio
2. Crear y activar entorno virtual
3. Instalar dependencias: `pip install django`
4. Ejecutar migraciones: `python manage.py migrate`
5. Crear superusuario: `python manage.py createsuperuser`
6. Iniciar servidor: `python manage.py runserver`

## Estructura

- `/blog/`: Aplicación principal
  - `models.py`: Contiene los modelos Post, Autor y Categoria
  - `forms.py`: Formularios para crear y buscar contenido
  - `views.py`: Lógica de las vistas
  - `templates/`: Plantillas HTML con herencia

## Accesos

- Página principal: http://localhost:8000/
- Admin: http://localhost:8000/admin/
- Crear Post: http://localhost:8000/post/nuevo/
- Buscar Posts: http://localhost:8000/buscar/
