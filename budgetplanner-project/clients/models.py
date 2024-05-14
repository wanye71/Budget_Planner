from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Client(models.Model):
    client_name = models.CharField(max_length=100)
    contact_phone = PhoneNumberField()
    contact_email = models.EmailField()
    contact_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    account_manager = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.client_name