from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    name = models.CharField(max_length=100)
    contact_information = models.CharField(max_length=200)
    industry = models.CharField(max_length=100)
    account_manager = models.ForeignKey(User, on_delete=models.CASCADE)