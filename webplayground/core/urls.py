from django.urls import path
from . import views
from .views import HomePageView,SamplePageView

"""
urlpatterns = [
    path('', views.home, name="home"),
    path('sample/', views.sample, name="sample"),
]
"""

# url de la clases internas

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('', SamplePageView.as_view(), name="sample")
]