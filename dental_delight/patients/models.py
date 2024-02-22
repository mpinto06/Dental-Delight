from django.db import models
from core.validators import only_int
from authuser.models import User

class Patient(models.Model):
    first_name = models.CharField(max_length=255, blank= False, null=False)
    last_name = models.CharField(max_length=255, blank= False, null=False)
    email = models.EmailField(unique=True, blank= False, null=False)
    phone_number = models.CharField(max_length=255, blank= False, null=False)
    citizen_number = models.CharField(max_length=255, validators=[only_int], unique=True, blank=False, null=False)
    created_by = models.ForeignKey(User, related_name='patients', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["first_name"]
    
    def get_short_name(self):
        return self.first_name
    
    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.get_full_name()
