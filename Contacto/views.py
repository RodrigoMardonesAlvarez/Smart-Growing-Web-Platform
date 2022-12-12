from django.shortcuts import render, redirect

from .forms import FormularioContacto

# Create your views here.

def contacto(request):
    formulario_contacto = FormularioContacto()
    
    if request.method == "POST":
        formulario_contacto = FormularioContacto(data = request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            telefono = request.POST.get("telefono")
            reunion = request.POST.get("reunion")
            proyecto = request.POST.get("proyecto")

            return redirect("/contacto/?validacion")

    
    return render(request, "Contacto/contacto.html", {'formularioCliente':formulario_contacto})
