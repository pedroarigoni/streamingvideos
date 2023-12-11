from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

LISTA_CATEGORIAS = (
    ("HUMOR", "Humor"),
    ("ACAO", "Ação"),
    ("CIENCIA", "Ciência"),
    ("HORROR", "Horror"),
    ("FANTASIA", "Fantasia"),
    ("OUTROS", "Outros"),
)
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=20, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)
    objects = models.Manager()

    def __str__(self):
        return self.titulo


# Episódios
class Episodio(models.Model):
    filme = models.ForeignKey("Filme", related_name="episodios", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self):
        return self.filme.titulo + ' - ' + self.titulo

class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField("Filme")
