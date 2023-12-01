# url - view - template

from django.urls import path, include
from .views import HomeVideos, HomePage

urlpatterns = [
    path('', HomePage.as_view()),
    path('videos/', HomeVideos.as_view())
]
