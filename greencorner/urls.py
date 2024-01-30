
from django.contrib import admin
from django.urls import path, include
from pages.views import get_index, get_menu, get_about, get_book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_index, name='get_index'),
    path('menu.html', get_menu, name='get_menu'),
    path('about.html', get_about, name='get_about'),
    path('index.html', get_index, name='get_index'),
    path('book.html', get_book, name='get_book'),
]
