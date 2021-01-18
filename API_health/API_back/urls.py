from django.urls import path

from .views import ProviderListView,DetailProvider ,get_nfz

urlpatterns=[
    path('',ProviderListView.as_view()),
    path('<int:pk>/',DetailProvider.as_view()),
    path('info',get_nfz, name='get_nfz')
]