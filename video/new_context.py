from .models import Filme

def lista_videos_recentes(request):
    lista_videos = Filme.objects.all().order_by("-data_criacao")[0:10]
    return {"lista_videos_recentes": lista_videos}

def lista_mais_vistos(request):
    lista_videos = Filme.objects.all().order_by("-visualizacoes")[0:10]
    return {"lista_mais_vistos": lista_videos}