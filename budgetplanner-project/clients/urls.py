from django.urls import path
from .views import ClientListView, ClientDetailView, CampaignListView, CampaignDetailView, ChannelDetailView, UpdateCampaignView

urlpatterns = [
    path('', ClientListView.as_view(), name='client_list'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('campaigns/<int:pk>/', CampaignDetailView.as_view(), name='campaign-detail'),
    path('update-campaign/', UpdateCampaignView.as_view(), name='update_campaign'),
]