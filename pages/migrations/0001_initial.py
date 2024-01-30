# Generated by Django 3.2.23 on 2024-01-30 14:06

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('number_of_people', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('table', models.TextField(choices=[('1', 'Table at the Bar'), ('2', 'Big Table'), ('3', 'Table With a View'), ('4', 'Table Made Of Ice')], max_length=255)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('time', models.TextField(choices=[('3-5', '3pm-5pm'), ('5-7', '5pm-7pm'), ('7-9', '7pm-9pm')], max_length=255)),
            ],
        ),
    ]