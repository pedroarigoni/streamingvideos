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