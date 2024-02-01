from django.forms import ModelForm
from django import forms
from .models import Reservation


tableChoices = [
    ('1', 'Table at the Bar'),
    ('2', 'Big Table'),
    ('3', 'Table With a View'),
    ('4', 'Table Made Of Ice')
]

sittingTimes = [('3-5', '3pm-5pm'), ('5-7', '5pm-7pm'), ('7-9', '7pm-9pm'),]


class Reserve_table_form(ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Full Name', 'style': 'width: 200px;', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email', 'style': 'width: 200px;', 'class': 'form-control'}))
    phone_number = forms.IntegerField(widget=forms.TextInput(
        attrs={'placeholder': 'Phone-number', 'style': 'width: 200px;', 'class': 'form-control'}))
    number_of_people = forms.IntegerField(widget=forms.NumberInput(
        attrs={'min': 1, 'max': '10', 'type': 'number', 'placeholder': 'Number of people', 'style': 'width: 200px;', 'class': 'form-control'}))
    table = forms.ChoiceField(choices=tableChoices, widget=forms.Select(
        attrs={'style': 'width: 200px;', 'class': 'form-control'}))
    date = forms.DateField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'type': 'date', 'style': 'width: 200px;'}))
    time = forms.ChoiceField(choices=sittingTimes, widget=forms.Select(
        attrs={'style': 'width: 200px;', 'class': 'form-control'}))

    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone_number',
                  'number_of_people', 'date', 'time', 'table']
