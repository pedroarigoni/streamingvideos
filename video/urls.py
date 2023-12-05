# url - view - template

from django.urls import path, include
from .views import HomeVideos, HomePage, DetalhesVideos


app_name = 'video'

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('videos/', HomeVideos.as_view(), name='homevideos'),
    path('videos/<int:pk>', DetalhesVideos.as_view(), name='detalhesvideos')
]
