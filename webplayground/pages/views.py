from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Page
# estos son objetos django con funciones especificas que nos permite trabajar de forma mas rapida
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
# Create your views here.
# E  ste es para una lista de respuesta


# Cambiamos la estructura Function Based Views a Class Based Views
# CBV nos permite trabajar desde clases para cargar los modelos y renderizar a la vistas he enviar datos de
# una consulta objetos,listas diccionarios o tuplas
class PagesListViews(ListView):
    model = Page


# Este es para un objeto de respuesta de uno
class PageDetailView(DetailView):
    model = Page


# Esta clase es para hacer un crete desde front-end
class PageCreateView(CreateView):
    model = Page
    fields = ['title', 'content', 'order']
    success_url = reverse_lazy('pages:pages')
    #def get_success_url(self):
        #return reverse('pages:pages')

"""
def pages(request):
    pages = get_list_or_404(Page)
    return render(request, pages/pages_.html, {'pages':pages})
# Este es para un objeto de respuesta de uno

def page(request, page_id, page_slug):
    page = get_object_or_404(Page, id=page_id)
    return render(request, pages/page_list.html, {'page':page})
"""