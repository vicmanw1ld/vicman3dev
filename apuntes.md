Para instalar Django:  
**mkdir <nombre del projecto **  
**pip install django**  
**pip install --upgrade pip**  
**python -m venv env**  
**source env/bin/activate**  
**django-admin startproject vicman3dev

**python manage.py runserver**  
manage.py es el script de gestión del proyecto

<image src="/home/vic/vicman3dev/imagenes/iniciar el servidor.png" alt="iniciamos el servidor">
corremos las migraciones:  

**python manage.py migrate**  

<image src="/home/vic/vicman3dev/imagenes/migrate.png" alt="migrate">  

**python manage.py createsuperuser**  
usuario 'vic'
correo '********@gmail.com'
password '**********'
Ponemos las credenciales en el projecto admin/ y tenemos todo el panel de administracion completo    

<image src="/home/vic/vicman3dev/imagenes/admin.png" alt="Admin">  

Vamos a empezar con la estructura de la página web, el proyecto se tratará de un blog en el que hablo sobre proyectos de impresión 3d así como de programación con Javascript y Python, un poco de mezcla de lo que me gusta hacer a mí.

La estructura sera:
**INDEXAPP** página principal:
1. PRESENTACIÓN
2. TÍTULO
3. INICIO
4. ENTRADAS BLOG
**LOGIN** login de la página:
1. nombre
2. apellidos
3. mail
4. password 
**BLOG** pulsar un blog e ir a la página.
**BASE DE DATOS**
1. nombre
2. apellidos
3. mail
4. password
5. fotos o enlaces a las fotos
6. dia de inicio
7. ...

empezamos creando indexapp:
```python
python3 manage.py startapp indexApp

# creamos un archivo en indexApp urls.py
from django.urls import path
from .views import index

urlpatterns = [
    path("index/",index, name='index'),
]
lo dejamos así para la primera función

# en el urls.py del projecto vicman3dev 
urlpatterns = [
    path('index/', include('indexApp.urls')),
    path("admin/", admin.site.urls),
]
lo dejamos así, incluimos el index en nuestro projecto vicman3dev

```
**HAY QUE BORRAR ESTO DESPUÉS**

**MODEL  TEMPLATE  VIEW
USUARIO -> SOLICITA A VIEW -> SOLICITA A MODEL -> QUE DEVUELVE A VIEW -> Y QUE ENSEÑA AL USUARIO EL TEMPLATE**

**indexApp** 
vamos a modelar la base de datos en models.py

```python
from django.db import models
from django.utils import timezone

class blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='indexApp/images')
    
    created_day = models.DateTimeField(default=django.utils.timezone.now)
    published_day = models.DateTimeField(blank=True, null=True)
    
    
    def __str__(self):
        return self.title # para que nos muestre el title en el blog
    
    class Meta:
        pass


```
 y lo agregamos al panel de admin.py

```python 
from django.contrib import admin
from .models import Blog

admin.site.register(Blog)

y migramos

python manage.py makemigrations

antes hay que registrar nuestra aplicación en settings.py de vicman3dev en INSTALLED APPS
errores:
instalar pilow que es la libreria que maneja errores en django y el datetime es asi from django.utils import timezone

python manage.py makemigrations
python manage.py migrate 

y ya nos da las migraciones 0001_initial.py podemos ver nuestra App
```

```python
vamos a views.py, para que nos muestre el modelo de la base de datos que hemos construido.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog


def index(request):
    blogerInfo = Blog.objects.all() # de este modelo blog trae todos los objetos
    return HttpResponse('hello world')

    return render(request, 'blogerInfo.html', {'blogerInfo': blogerInfo}) # renderizamos el template que le vamos a pasar en este caso bloguer.html, y ademas le pasamos toda la información que hay en la clase Blog a traves de la variable blogerInfo, y ahora pasamos abajo a el html

#Creamos una carpeta dentro de indexApp llamada templates
#dentro de esta el archivo bloger.html
# Lo damos de alta en vicman3dev en settings en la carpeta templates

```
<image src="/home/vic/vicman3dev/imagenes/settings templates.png" alt="settings templates">


Podemos ver que funciona con el comando en consola python manage.py shell

<image src="/home/vic/vicman3dev/imagenes/Captura de pantalla de 2023-02-10 09-31-03.png" alt="manage.py shell">

se puede solicitar por id también:
```python 
python manage.py shell
from Blog.models import blog

Blog.objects.all()
Blog.objects.get(id = 1)
Blog.objects.filter(name='nevado y shin chan')

```
**Renderizar el html para que se vea todo el blog**

creamos la carpeta templates y dentro de esta el blogerInfo.html y quedaría de este modo pasándole toda la info del view:

<image src="/home/vic/vicman3dev/imagenes/bloger html.png" alt="blogerInfo.html">

si corremos el servidor podemos ver todo salvo las imagenes, hay que ir a urls del proyecto vicman3dev y poner lo siguiente:
```python
from django.urls import path
from .views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",index, name='index'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

```
Ahora ya podemos ver todas las imágenes y el admin también

Vamos a recuperar un solo blog con el boton de ver mas...

```python
# esta es una función para traer un blog por el id, en nuestro caso solo hay 1 asi que será el 1

**views.py** de indexApp 

def get_titleBlog(request, id):
    getBlog = Blog.objects.get(id=id)

    return render(request, 'getBlog.html', {'getBlog' : getBlog})
```
**urls.py** de indexApp
```python
urlpatterns = [
    path("",views.index, name='index'),
    path("getBlog/<int:id>", views.get_titleBlog, name='get_titleBlog' )

] 
```
<image src="/home/vic/vicman3dev/imagenes/getBlog-2.png" alt="getBlog-2">

**CONECTANDO A LA BASE DE DATOS**

 https://docs.djangoproject.com/en/4.1/ref/settings/#databases

Para ello vamos a settings.py del proyecto vicman3dev, y en Databases, la configuramos:

```python
DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'vicman3dev_db',
        'USER': 'vicman3dev',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

```
**CONSOLA**

```mysql
sudo mysql -u root

CREATE DATABASE vicman3dev;
```
Por si nos da algún error podemos instalar pymsql:
**pip install pymsql**
y lo importamos en el settings del proyecto:

**from pathlib import Path
import pymsql**
por si acaso mirar el video en minuto 6:00 de formularios en django

python manage.py migrate Para las migraciones

y pip freeze > requeriments.txt

en el settings
```python
import pimysql
y encima de la base de datos 

pymysql.version_info = (1,4,2, 'final', 0)
pymysql.install_as_MySQLdb()

```
Al final despues de varios fallos, he creado un nuevo usuario en mysql:
```mysql
CREATE USER nombreusuario@localhost IDENTIFIED BY 'pass';
GRANT ALL PRIVILEGES ON nombreDB.* TO nombreusuario@localhost;
FLUSH PRIVILEGES;
```
y así es más fácil para conectar con la base de datos.
Al haber conectado con la base de datos se ha borrado todo, por lo que volvemos a crear el superusuairo
```python
(env) (base) vic@vic-Mint:vicman3dev/vicman3dev ‹master*›$ python manage.py createsuperuser
Username (leave blank to use 'vic'): vicman3dev
Email address: victor3dev@gmail.com
Password: 
Password (again): 
Superuser created successfully.

```
ya conecta perfecto
En el html conecta bien al leer más: 

**STATICFILES**
Creamos una carpeta de archivos estáticos con styles.css para que la lea globalmente, se coloca en settings del proyecto:
```python
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / 'staticFiles'
]
```
**CARPETA EN LOCAL Y CARPETA EN PRODUCCIÓN**

Vamos a crear dos carpetas para ver cual nos queda en local y cual en producción.
Creamos una carpeta dentro del proyecto vicman3dev llamada settings y dentro de esta base.py, del archivo general de settings lo cortamos y lo pegamos en base.py. Borramos el archivo vací de settings, creamos dentro del nuevo settings local.py que va a ser donde guardemos la confi local. y otro para prod.py 
en el archivo local.py le pasamos lo siguiente:

```python
importamos el archivo base y la base de datos
from .base import *
import pymysql

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

pymysql.version_info = (1,4,2, 'final', 0)
pymysql.install_as_MySQLdb()

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "vicman3dev",
        "USER": "vicman3dev",
        "PASSWORD": "pass",
        "HOST": "localhost",
        "PORT": "3306"
    }
}
tambien traemos:

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost']


```
En prod.py, va a ir la misma conf de la base de datos:
```python
from .base import *
import os
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "vicman3dev",
        "USER": "vicman3dev",
        "PASSWORD": "pass",
        "HOST": "localhost",
        "PORT": "3306"
    }
}

```
para no traernos la conf a prod.py configuraremos variables de ambiente:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ['DATABASE_NAME'],
        "USER": os.environ['DATABASE_USER'],
        "PASSWORD": os.environ['DATABASE_PASSWORD'],
        "HOST": os.environ['DATABASE_HOST'],
        "PORT": os.environ['DATABASE_PORT'],
    }
}
```
si corremos el proyecto no va a funcionar pq hemos borrado el archivo settings hay que decirle donde se encuentra el nuevo archivo
```python
python manage.py runserver --settings=settings.local
hay que pasarlo siempre así para todo

```
hay un truco para esto, creamos el archivo 'Makefile' y dentro de este ponemos el comando que queremos que corra:
run:
    python manage.py runserver --settings=settings.local
si corremos en consola make run comienza el servidor    