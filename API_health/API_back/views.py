from rest_framework import generics
from .models import ProviderNHS
from .serializers import ProviderSerializer

class ProviderListView(generics.ListAPIView):
    queryset = ProviderNHS.objects.all()
    serializer_class = ProviderSerializer


class DetailProvider(generics.RetrieveAPIView):
    queryset = ProviderNHS.objects.all()
    serializer_class = ProviderSerializer


from django.shortcuts import render
import requests

def get_nfz(request):
    response=requests.get("https://api.nfz.gov.pl/app-itl-api/queues?format=json&case=1&province=01&benefitForChild=true&api-version=1.3")

    odp = response.json()['data']
    provider=[]
    locality=[]
    regons=[]
    benefits=[]
    covid=[]
    for d in odp:
        provider.append(d['attributes']['provider'])
        locality.append(d['attributes']['locality'])
        regons.append(d['attributes']['regon-provider'])
        covid.append(d['attributes']['covid-19'])
        benefits.append(d['attributes']['benefit'])

    return render(request, 'API_back/nfz_info.html',{
        'provider':provider,
        'local':locality,
        'regons':regons,
        'covid':regons,
        'benefits':benefits
    })