from rest_framework import generics
from .models import ProviderNHS
from .serializers import ProviderSerializer

class ProviderListView(generics.ListAPIView):
    queryset = ProviderNHS.objects.all()
    serializer_class = ProviderSerializer


class DetailProvider(generics.RetrieveAPIView):
    queryset = ProviderNHS.objects.all()
    serializer_class = ProviderSerializer