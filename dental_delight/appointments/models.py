from django.db import models
from patients.models import Patient
from dentists.models import Dentist

class Appointment(models.Model):
    date = models.DateTimeField(blank=False, null=False)
    description = models.TextField(blank=True)
    patient = models.ForeignKey(Patient, related_name = 'appointments', on_delete=models.CASCADE, blank=False, null=False)
    dentists = models.ManyToManyField(Dentist, related_name='appointments')

