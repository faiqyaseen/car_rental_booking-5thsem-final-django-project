from ast import Call
from pyexpat import model
from tkinter import CASCADE
from typing import Callable
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

from .validators import validate_file_extension
# Create your models here.

class Brands(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    logo = models.FileField(upload_to='static/main/images/', validators=[validate_file_extension])

    def __str__(self):
        return self.name

class Vehicles(models.Model):
    brand_id = models.ForeignKey(Brands, on_delete=Call)
    name = models.CharField(max_length=40)
    model = models.CharField(max_length=40)
    status = models.IntegerField()
    rent_per_hour = models.FloatField()
    description = models.TextField()
    image = models.FileField(upload_to='static/main/images/', validators=[validate_file_extension])

    def __str__(self):
        return self.name

class Booking(models.Model):
    vehicle = models.ForeignKey(Vehicles, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pick_location = models.CharField(max_length=40, default="")
    drop_location = models.CharField(max_length=40, default="")
    pick_date = models.DateField(default=now)
    drop_date = models.DateField(default=now)
    pick_time = models.CharField(max_length=40)
    status = models.IntegerField(default=2)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.user.username + " " + self.drop_location
