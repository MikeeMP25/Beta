from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "core/home.html"
    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()[:5]
        return context
    """
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': "Welcome a my page playground"})


# def home(request):
#    return render(request, "core/home.html")

class SamplePageView(TemplateView):
    template_name = "core/sample.html"
