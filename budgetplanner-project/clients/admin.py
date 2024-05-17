from django.contrib import admin
from .models import Client, Campaign, BudgetAllocation, Channel


class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'contact_name', 'contact_phone', 'contact_email', 'account_manager_name',)

    def account_manager_name(self, obj):
        return f"{obj.account_manager.first_name} {obj.account_manager.last_name}"
    account_manager_name.short_description = 'Account Manager'
admin.site.register(Client, ClientAdmin)

class CamapaignAdmin(admin.ModelAdmin):
    list_display = ('campaign_name', 'client_name', 'budget_amount', 'start_date', 'end_date')
admin.site.register(Campaign, CamapaignAdmin)

class BudgetAllocationAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'budget_amount', 'start_date', 'end_date')

admin.site.register(BudgetAllocation, BudgetAllocationAdmin)

admin.site.register(Channel)