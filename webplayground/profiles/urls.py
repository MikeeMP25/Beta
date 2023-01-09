from django.urls import path
from .views import ProfilesListView, PerfileDetailView

profiles_patterns=([
    path('', ProfilesListView.as_view(), name='list'),
    path('<username>/', PerfileDetailView.as_view(), name="detail"),
], "profiles")