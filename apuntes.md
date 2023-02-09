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

