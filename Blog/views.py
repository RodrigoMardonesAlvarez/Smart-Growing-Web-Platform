from django.shortcuts import render
from Blog.models import Entrada

# Create your views here.

def blog(request):
    
    entradas=Entrada.objects.all()
    return render(request, "blog/blog.html", {"entradas":entradas})

