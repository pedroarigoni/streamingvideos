from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView

# Create your views here.
class HomePage(TemplateView):
    template_name = "homepage.html"

# url - view - html
class HomeVideos(ListView):
    template_name = "homevideos.html"
    model = Filme
