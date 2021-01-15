from rest_framework import  serializers
from .models import ProviderNHS

class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model=ProviderNHS
        fields=('id','benefit' ,'provider' ,'locality' , 'regon_provider' ,'covid_19')

