from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Client, Campaign, Channel

# Client Views
class ClientListView(ListView):
    model = Client
    template_name = 'client/client_list.html'  # Create this template in your templates directory
    context_object_name = 'clients'

class ClientDetailView(DetailView):
    model = Client
    template_name = 'client/client_detail.html'  # Create this template in your templates directory
    context_object_name = 'client'
    
    def get_context_data(self, **kwargs):
        # Get the existing context from DetailView
        context = super().get_context_data(**kwargs)
        # Add the campaigns related to this client to the context
        context['campaigns'] = Campaign.objects.filter(client_name=self.object)
        return context

class ClientCreateView(CreateView):
    model = Client
    template_name = 'client/client_form.html'  # Create this template in your templates directory
    fields = ['client_name', 'contact_phone', 'contact_email', 'contact_name', 'industry', 'account_manager']
    success_url = reverse_lazy('client_list')  # Redirect to the client list view upon successful creation

class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'client/client_form.html'  # Create this template in your templates directory
    fields = ['client_name', 'contact_phone', 'contact_email', 'contact_name', 'industry', 'account_manager']
    context_object_name = 'client'
    success_url = reverse_lazy('client_list')  # Redirect to the client list view upon successful update

class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'client/client_confirm_delete.html'  # Create this template in your templates directory
    success_url = reverse_lazy('client_list')  # Redirect to the client list view upon successful deletion


# Campaign Views

class CampaignListView(ListView):
    model = Campaign
    template_name = 'client/campaign_list.html'  # Create a template named 'campaign_list.html' to display the list of campaigns
    context_object_name = 'campaigns'  # Define the context variable name for the list of campaigns

class CampaignDetailView(DetailView):
    model = Campaign
    template_name = 'client/campaign_detail.html'  # Create a template named 'campaign_detail.html' to display the details of a campaign
    context_object_name = 'campaign'  # Define the context variable name for the campaign object

# Channel Views    
class ChannelDetailView(DeleteView):
    model = Channel
    template_name = 'client/campaign_detail.html'
    context_object_name = 'channel'