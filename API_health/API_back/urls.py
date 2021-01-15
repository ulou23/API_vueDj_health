from django.urls import path

from .views import ProviderListView

urlpatterns=[
    path('', ProviderAPIView.as_view(),name='home')
]