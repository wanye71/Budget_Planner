from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver

class Client(models.Model):
    client_name = models.CharField(max_length=100)
    contact_phone = PhoneNumberField()
    contact_email = models.EmailField()
    contact_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    account_manager = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.client_name
    
class Campaign(models.Model):
    campaign_name = models.CharField(max_length=100)
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE)
    budget_amount = models.DecimalField(max_digits=100, decimal_places=2)  # Add a budget amount field
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.campaign_name

class BudgetAllocation(models.Model):
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='budget_allocations_associated')
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    budget_amount = models.DecimalField(max_digits=100, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    @property
    def remaining_budget(self):
        campaigns_total_budget = self.campaigns.aggregate(total_budget=models.Sum('budget_amount'))['total_budget']
        return self.budget_amount - (campaigns_total_budget or 0)

@receiver(post_save, sender=Campaign)
def update_budget_allocation(sender, instance, created, **kwargs):
    if created:
        budget_allocation = instance.client_name.budget_allocations_associated.get(channel=instance.channel)
        budget_allocation.budget_amount -= instance.budget_amount
        budget_allocation.save()