from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
from django.forms import ValidationError
from django.http import HttpResponseRedirect

sittingTimes = (
    ("3-5", "3pm-5pm"),
    ("5-7", "5pm-7pm"),
    ("7-9", "7pm-9pm"),
)

tableChoices = [
    ('1', 'Table at the Bar'),
    ('2', 'Big Table'),
    ('3', 'Table With a View'),
    ('4', 'Table Made Of Ice')
]


class Reservation(models.Model):
    name = models.CharField(max_length=55)
    email = models.EmailField()
    phone_number = models.IntegerField()
    number_of_people = models.IntegerField(validators=[MinValueValidator(0),
                                                       MaxValueValidator(5)])
    table = models.TextField(choices=tableChoices, max_length=255)
    date = models.DateTimeField(default=datetime.now)
    time = models.TextField(choices=sittingTimes, max_length=255)

    def __str__(self):
        return self.name


class Meta:
    constraints = [
        models.UniqueConstraint(
            fields=['table', 'date', 'time'], name='unique_table_date_time')
    ]
