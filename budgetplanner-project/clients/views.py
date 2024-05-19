from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from .models import Client, Campaign, Channel,BudgetAllocation
from django.contrib.auth.decorators import login_required
from .forms import CampaignForm


# Client Views

class ClientListView(ListView):
    model = Client
    template_name = 'client/client_list.html'  # Create this template in your templates directory
    context_object_name = 'clients'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

class ClientDetailView(DetailView):
    model = Client
    template_name = 'client/client_detail.html'  # Create this template in your templates directory
    context_object_name = 'client'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        # Get the existing context from DetailView
        context = super().get_context_data(**kwargs)
        client = self.object
        # Add the campaigns related to this client to the context
        context['campaigns'] = Campaign.objects.filter(client_name=self.object)
        context['budget_allocation'] = BudgetAllocation.objects.filter(client_name=client).first()
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
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

class UpdateCampaignView(View):
    template_name = 'clients/client_detail.html'

    def get(self, request):
        campaigns = Campaign.objects.all()
        return render(request, self.template_name, {'campaigns': campaigns})

    def post(self, request):
        campaign_id = request.POST.get('campaign')
        budget_amount = request.POST.get('budget_amount')

        campaign = Campaign.objects.get(pk=campaign_id)
        campaign.budget_amount = budget_amount
        campaign.save()

        return redirect('client_detail', pk=campaign.client_name.pk)

class CampaignDetailUpdateView(View):
    template_name = 'client/campaign_detail.html'

    def get(self, request, *args, **kwargs):
        campaign = get_object_or_404(Campaign, id=kwargs['pk'])
        form = CampaignForm(instance=campaign)
        return render(request, self.template_name, {'form': form, 'campaign': campaign})

    def post(self, request, *args, **kwargs):
        campaign = get_object_or_404(Campaign, id=kwargs['pk'])
        form = CampaignForm(request.POST, instance=campaign)
        if form.is_valid():
            form.save()
            return redirect('campaign-detail', pk=campaign.pk)
        return render(request, self.template_name, {'form': form, 'campaign': campaign})

# Channel Views    
class ChannelDetailView(DeleteView):
    model = Channel
    template_name = 'client/campaign_detail.html'
    context_object_name = 'channel'
    
# Login View
class LoginView(View):
    form_class = LoginForm
    template_name = 'client/login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('client/')
        return render(request, self.template_name, {'form': form})