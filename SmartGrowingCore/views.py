from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):

    return render(request, "SmartGrowingApp/home.html")

def productos(request):
    
    return render(request, "SmartGrowingApp/productos.html")


def desarrollo(request):
    
    return render(request, "SmartGrowingApp/desarrollo.html")

def contacto(request):
    
    return render(request, "SmartGrowingApp/contacto.html")
