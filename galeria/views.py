from django.shortcuts import render,get_object_or_404
from galeria.models import Fotografia
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

# Testando autenticação nas views 
# https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django/Authentication


@login_required
def index(request):
   
   fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
   
   return render(request, 'galeria/index.html', {"cards":fotografias})

@permission_required('galeria.buscar_no_site')
def buscar(request):
   fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

   if "buscar" in request.GET:
      nome_a_buscar = request.GET['buscar']
      if nome_a_buscar:
         fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

   return render(request, 'galeria/buscar.html',{"cards":fotografias})

@login_required
def imagem(request,foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    
    return render(request, 'galeria/imagem.html', {"fotografia":fotografia})
