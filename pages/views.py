from django.shortcuts import render
from django.views import generic
from .models import Reservation
from django.shortcuts import render
from .forms import Reserve_table_form
from django.contrib import messages


# Create your views here.


def get_index(request):
    return render(request, 'pages/index.html')


def get_menu(request):
    return render(request, 'pages/menu.html')


def get_about(request):
    return render(request, 'pages/about.html')


def get_book(request):
    if request.POST:
        form = Reserve_table_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking succesful!')
        else:
            messages.add_message(request, messages.WARNING,
                                 'Sorry, that time and table is already taken. Try another!')
            return render(request, 'restaurant/book.html', {'form': Reserve_table_form})
    return render(request, 'restaurant/book.html', {'form': Reserve_table_form})
