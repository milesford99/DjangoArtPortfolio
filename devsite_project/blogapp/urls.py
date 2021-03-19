from django.urls  import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('video', views.video, name='video'),
    path('art', views.art, name='art'),
    path('music', views.music, name='music'),
]