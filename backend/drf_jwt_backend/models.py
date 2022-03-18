from datetime import datetime
import email
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


class Survivor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    warrior = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    datetime = models.IntegerField()
