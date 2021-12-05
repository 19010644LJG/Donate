from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Donate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    donation = models.CharField(max_length=10,unique=False)
    select = models.CharField(max_length=5,unique=False)
    accept = models.CharField(max_length=10, default='승인대기')