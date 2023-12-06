from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.
class HomePage(TemplateView):
    template_name = "homepage.html"

# url - view - html
class HomeVideos(ListView):
    template_name = "homevideos.html"
    model = Filme

class DetalhesVideos(DetailView):
    template_name = "detalhesvideo.html"
    model = Filme

    def get_context_data(self, **kwargs):
        context = super(DetalhesVideos, self).get_context_data(**kwargs)
        videos_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]
        context["videos_relacionados"] = videos_relacionados
        return context