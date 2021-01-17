from django.urls import path

from .views import ProviderListView,DetailProvider

urlpatterns=[
    path('',ProviderListView.as_view()),
    path('<int:pk>/',DetailProvider.as_view()),
]