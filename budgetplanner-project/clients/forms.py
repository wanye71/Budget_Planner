# forms.py
from django import forms
from .models import Campaign

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(widget=forms.PasswordInput)

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['description']