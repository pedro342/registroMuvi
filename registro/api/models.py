from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    mail = models.EmailField(max_length=100, unique=True)