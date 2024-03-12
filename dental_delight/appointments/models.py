from django.db import models
from patients.models import Patient
from dentists.models import Dentist
from authuser.models import User

class Appointment(models.Model):
    date = models.DateField(blank=False, null=False)
    time = models.TimeField(blank=True, null=True)
    description = models.TextField(blank=True)
    patient = models.ForeignKey(Patient, related_name = 'appointments', on_delete=models.CASCADE, blank=False, null=False)
    dentists = models.ManyToManyField(Dentist, related_name='appointments')
    created_by = models.ForeignKey(User, related_name='appointments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
