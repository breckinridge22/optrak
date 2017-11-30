from django.db import models

# Create your models here.

# when a new provider is created -- create a key pair and store the id on the chain
class Provider(models.Model):
    name = models.CharField(max_length = 20)

# when a new provider is created -- create a key pair and store the id on the chain
class Physician(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    physicianID = models.IntegerField(max_length = 20)
    

# when a new patient is created -- create a key pair and store the id on the chain
class Patient(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)

class Prescription(models.Model):
    #dbdbdb
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, blank=True, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
    drugId = models.IntegerField(default = 0)
    dosage = models.IntegerField(default = 0)
    dateWritten = models.DateField(auto_now_add=False, null=True)
    dateFilled = models.DateField(auto_now_add=False, null=True)

class Request(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, blank=True, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)

class Response(models.Model):
     STATUS_CHOICES = (('0', 'Failure'), ('1', 'Success'))
     provider = models.ForeignKey(Provider, on_delete=models.CASCADE, blank=True, null=True)
     patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
     status = models.CharField(max_length=1, choices=STATUS_CHOICES)
