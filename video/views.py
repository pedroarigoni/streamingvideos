from django.shortcuts import redirect, reverse
from .models import Filme
from .forms import CriarContaForm
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomePage(TemplateView):
    template_name = "homepage.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('video:homevideos')
        else:
            return super().get(request, *args, **kwargs)

# url - view - html
class HomeVideos(LoginRequiredMixin, ListView):
    template_name = "homevideos.html"
    model = Filme

class DetalhesVideos(LoginRequiredMixin, DetailView):
    template_name = "detalhesvideo.html"
    model = Filme

    def get(self, request, *args, **kwargs):
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()
        usuario = request.user
        usuario.filmes_vistos.add(filme)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DetalhesVideos, self).get_context_data(**kwargs)
        videos_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]
        context["videos_relacionados"] = videos_relacionados
        return context

class PesquisaVideo(LoginRequiredMixin, ListView):
    template_name = "pesquisa.html"
    model = Filme

    def get_queryset(self):
        pesquisa = self.request.GET.get('query')
        if pesquisa:
            object_list = self.model.objects.filter(titulo__icontains=pesquisa, descricao__icontains=pesquisa)
            return object_list
        else:
            return None
class EditarPerfil(LoginRequiredMixin, TemplateView):
    template_name = "editarperfil.html"

class CriarConta(FormView):
    template_name = "criarconta.html"
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('video:login')

