from django.shortcuts import render
from django.views import generic

# Create your views here.


def get_index(request):
    return render(request, 'pages/index.html')


def get_menu(request):
    return render(request, 'pages/menu.html')


def get_about(request):
    return render(request, 'pages/about.html')
