from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog


'''def index(request):
    blogerInfo = Blog.objects.all() # de este modelo blog trae todos los objetos
    
    return render(request, 'blogerInfo.html', {'blogerInfo': blogerInfo})'''

def index(request):
    ppal =  Blog.objects.all()
    return render(request, 'index.html', {'ppal': ppal})  

def blog(request):
    blogerInfo = Blog.objects.all() # de este modelo blog trae todos los objetos
    
    return render(request, 'blogerInfo.html', {'blogerInfo': blogerInfo})


def get_titleBlog(request, id):
    getBlog = Blog.objects.get(id=id)

    return render(request, 'getBlog.html', {'getBlog' : getBlog})