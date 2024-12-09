# Proyecto para Curso Python CoderHouse

Este es un proyecto desarrollado en Django que permite crear un blog donde los usuarios pueden publicar posts, agregar categorías, comentar en los posts, realizar búsquedas de post y filtrar por categoría de post. Le di una temática al blog donde en teoría se postearía experiencias malas de trabajo.

## Requisitos

- Python 3.x
- Django 3.x o superior

## Instalación

1. Clona el repositorio en tu máquina local:

   '''bash
   git clone https://github.com/RayRivero/TuPrimeraPagina-Rivero.git

2. Crea un entorno virtual:

   '''bash
python -m venv env
source env/bin/activate  # En Mac/Linux
env\Scripts\activate  # En Windows

3. Instala las dependencias:

   '''bash
pip install django

4. Realiza las migraciones para crear la base de datos:

   '''bash
python manage.py migrate

5. Ejecuta el servidor de desarrollo:

   '''bash
python manage.py runserver

6. Accede a la aplicación desde tu navegador en: http://127.0.0.1:8000

FUNCIONALIDADES:

Están presentes justo de bajo del titulo de la pagina "El cliente NO siempre tiene la razon"

(se mencionara la palabra usuario en estas descripciones, sin embargo no se agrego ningún login en la pagina ya que no se creyó necesario en esta consigna. Usuario sera cualquiera con acceso a la pagina en este caso.)

**Publicar Posts**: Los usuarios pueden crear y publicar post con titulo y seleccionar una categoría para el post.

**Agregar Categoría**: Usuarios podrán agregar categorías nuevas para que se puedan asignar a los posts.

**Comentar los Posts**: Los usuarios pueden dejar comentarios en posts ya existentes.

**Búsqueda de Posts**: Los usuarios podrán realizar búsqueda de caracteres para encontrar posts que contengan los mismos.

**Filtrar por Categoría**: En lugar de buscar algún post especifico, la pagina ofrece mostrar todos los posts de cierta categoría elegida.




