# simulation/resources.py
from tastypie.resources import ModelResource
from simulation.models import Prescription
from tastypie.authentication import ApiKeyAuthentication

from django.contrib.auth.models import User

class PrescriptionResource(ModelResource):
    class Meta:
        queryset = Prescription.objects.all()
        resource_name = 'prescription'
        authorization = ApiKeyAuthentication()
