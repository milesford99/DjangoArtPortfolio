from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
# Create your views here.

def index(request):
    blogposts = Blogpost.objects.all()

    context = {
        'blogposts': blogposts
    }
    return render(request, 'blogapp/index.html', context)

def video(request):
    return render(request, 'blogapp/video.html')

def art(request):
    return render(request, 'blogapp/art.html')

def music(request):
    return render(request, 'blogapp/music.html')

