from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name='index'),
    path("blog/", views.blog, name='blog' ),
    path("getBlog/<int:id>", views.get_titleBlog, name='get_Blog' )

] 