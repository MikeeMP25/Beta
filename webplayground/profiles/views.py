from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registration.models import Profiles


# Create your views here.
class ProfilesListView(ListView):
    model = Profiles
    template_name = 'profiles/profile_list.html'
    paginate_by = 2


class PerfileDetailView(DetailView):
    model = Profiles
    template_name = 'profiles/profile_detail.html'

    def get_object(self):
        return get_object_or_404(Profiles, user__username=self.kwargs["username"])