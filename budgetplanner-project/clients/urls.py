from django.urls import path
from django.contrib.auth import views as auth_views
from .views import ClientListView, ClientDetailView, CampaignListView, CampaignDetailView, ChannelDetailView, UpdateCampaignView, LoginView

urlpatterns = [
    path('', LoginView.as_view(), name='admin_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('client/', ClientListView.as_view(), name='client_list'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('campaigns/<int:pk>/', CampaignDetailView.as_view(), name='campaign-detail'),
    path('update-campaign/', UpdateCampaignView.as_view(), name='update_campaign'),
]