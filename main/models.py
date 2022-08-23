from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    comment = models.TextField()

