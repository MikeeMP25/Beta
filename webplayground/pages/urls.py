from django.urls import path
from .views import *

"""
urlpatterns = [
    path('', views.pages, name='pages'),
    path('<int:page_id>/<slug:page_slug>/', views.page, name='page'),
]"""

pages_patterns = ([
    path('', PagesListViews.as_view(), name="pages"),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name="page"),
    path('create/', PageCreateView.as_view(), name="create"),
    path('update/<int:pk>/', PageUpdateView.as_view(), name="update"),
    path('dalete/<int:pk>/', PageDeleteView.as_view(), name="delete"),
], "pages")

# como cambiamos a clase con modelos directos cuando mandamos la id por la url de int:page_id a
# int:pk pk= lo detecta directamente como un atributo primary key