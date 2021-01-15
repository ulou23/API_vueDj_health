from django.db import models

class ProviderNHS(models.Model):
    benefit =models.CharField(max_length=100)
    provider=models.CharField(max_length=100)
    locality=models.CharField(max_length=80)
    regon_provider=models.IntegerField(default=0)
    covid_19=models.CharField(max_length=10)
