from django.contrib import admin
from .models import Client, Campaign, BudgetAllocation, Channel

admin.site.register(Client)
admin.site.register(Campaign)

class BudgetAllocationAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'budget_amount', 'start_date', 'end_date')

admin.site.register(BudgetAllocation, BudgetAllocationAdmin)
admin.site.register(Channel)