from django.urls import path
from .views import ClientListView, ClientDetailView, CampaignListView, CampaignDetailView, ChannelDetailView

urlpatterns = [
    path('', ClientListView.as_view(), name='client_list'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('campaigns/<int:pk>/', CampaignDetailView.as_view(), name='campaign-detail'),
]