from django.shortcuts import render
from Blog.models import Entrada
from django.core.paginator import Paginator
# Create your views here.

def blog(request):
    
    listado_entradas=Entrada.objects.all()
    paginator = Paginator(listado_entradas, 2)
    pagina = request.GET.get("page") or 1
    entradas = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, entradas.paginator.num_pages +1 )
    return render(request, "blog/blog.html", {"entradas":entradas, "paginas": paginas, "pagina_actual": pagina_actual})

