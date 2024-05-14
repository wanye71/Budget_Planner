from django.contrib import admin
from .models import Client, Campaign, BudgetAllocation, Channel

admin.site.register(Client)
admin.site.register(Campaign)
admin.site.register(BudgetAllocation)
admin.site.register(Channel)