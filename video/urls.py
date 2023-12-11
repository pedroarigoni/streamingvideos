# url - view - template

from django.urls import path, include
from .views import HomeVideos, HomePage, DetalhesVideos, PesquisaVideo
from django.contrib.auth import views as auth_view

app_name = 'video'

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('videos/', HomeVideos.as_view(), name='homevideos'),
    path('videos/<int:pk>', DetalhesVideos.as_view(), name='detalhesvideos'),
    path('pesquisa/', PesquisaVideo.as_view(), name='pesquisavideo'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
]
