from django.urls import path
from django.contrib.auth import views as auth_views
from .views import ClientListView, ClientDetailView, CampaignListView, CampaignDetailView, ChannelDetailView, UpdateCampaignView, LoginView, CampaignDetailUpdateView

urlpatterns = [
    # path('', LoginView.as_view(), name='admin_login'),
    
    path('', auth_views.LoginView.as_view(template_name='client/login.html'), name='login'),
    
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    
    path('client/', ClientListView.as_view(), name='client_list'),
    
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    
    path('campaigns/<int:pk>/', CampaignDetailView.as_view(), name='campaign-detail'),
    
    path('update-campaign/', UpdateCampaignView.as_view(), name='update_campaign'),
    
    path('campaign/<int:pk>/update/', CampaignDetailUpdateView.as_view(), name='campaign_detail_update'),

]