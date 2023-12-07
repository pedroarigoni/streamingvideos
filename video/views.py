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

    def get(self, request, *args, **kwargs):
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DetalhesVideos, self).get_context_data(**kwargs)
        videos_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]
        context["videos_relacionados"] = videos_relacionados
        return context

class PesquisaVideo(ListView):
    template_name = "pesquisa.html"
    model = Filme

    def get_queryset(self):
        pesquisa = self.request.GET.get('query')
        if pesquisa:
            object_list = self.model.objects.filter(titulo__icontains=pesquisa, descricao__icontains=pesquisa)
            return object_list
        else:
            return None
