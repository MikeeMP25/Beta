from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Page
# estos son objetos django con funciones especificas que nos permite trabajar de forma mas rapida
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .forms import PageForm
from django.shortcuts import redirect


# Create your views here.
# aqui creamos la clase principal que operar el dispanchas
class StaffRequiredMixin(object):
    """Este mixin requerira que el usuario sea miembro el staff  """
    # Aqui rescribimos un metodo ahora le damos ciertos permisos a la vista
    # que solo los usuario logias y registrados pueden ver la vista create en caso contrario
    # los renderiza al login..!!
    @method_decorator(staff_member_required())
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


# Este es para una lista de respuesta
""" ESTO ES EN MODO LECTURA"""
# Cambiamos la estructura Function Based Views a Class Based Views
# CBV nos permite trabajar desde clases para cargar los modelos y renderizar a la vistas he enviar datos de
# una consulta objetos,listas diccionarios o tuplas


class PagesListViews(ListView):
    model = Page


# Este es para un objeto de respuesta de uno
class PageDetailView(DetailView):
    model = Page


""" ESTO ES EN MODO ESCRITURA Y LECTURA (MANIPULABLE O EDITABLE)"""


# Esta clase es para hacer un crete desde front-end
@method_decorator(staff_member_required(), name='dispatch')
class PageCreateView(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')

# def get_success_url(self):
# return reverse('pages:pages')


@method_decorator(staff_member_required(), name='dispatch')
class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'


@method_decorator(staff_member_required(), name='dispatch')
class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')


"""
def pages(request):
    pages = get_list_or_404(Page)
    return render(request, pages/pages_.html, {'pages':pages})
# Este es para un objeto de respuesta de uno

def page(request, page_id, page_slug):
    page = get_object_or_404(Page, id=page_id)
    return render(request, pages/page_list.html, {'page':page})
"""
