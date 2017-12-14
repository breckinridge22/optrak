
from django.db import models

# Create your models here.
class Prescription(models.Model):
    #dbdbdb
    #patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
    drugId = models.CharField(max_length = 20)
    quantity = models.IntegerField(default = 0)
    days = models.IntegerField(default = 0)
    dateWritten = models.DateField(auto_now_add=False, null=True)
    dateFilled = models.DateField(auto_now_add=False, null=True)
    rxNumber = models.IntegerField(default = 0)
    refills = models.IntegerField(default = 0)

def __str__(self):
    return '%s %d' % (self.drugId, self.quantity)
