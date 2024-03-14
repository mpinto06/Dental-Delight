from django.db import models
from core.validators import only_int
from authuser.models import User

class Dentist(models.Model):
    first_name = models.CharField(max_length=255, blank= False, null=False)
    last_name = models.CharField(max_length=255, blank= False, null=False)
    email = models.EmailField(unique=True, blank= False, null=False)
    phone_number = models.CharField(max_length=255, blank= False, null=False)
    citizen_number = models.CharField(max_length=255, validators=[only_int], unique=True, blank=False, null=False)
    ENDODONTIST  = 'endodontist'
    ORTHODONTIST = 'orthodontist'
    PERIODONTIST = 'periodontist'
    PROSTHODONTIST = 'prosthodontist'
    MAXILLOFACIAL_SURGEON = 'maxillofacial_surgeon'
    MAXILLOFACIAL_RADIOLOGIST = 'maxillofacial_radiologist'
    ANESTHESIOLOGISTS = 'anesthesiologists'
    MAXILLOFACIAL_PATHOLOGIST = 'maxillofacial_pathologist'
    PEDIATRIC_DENTIST = 'pediatric_dentist'
    OROFACIAL_PAIN = 'orofacial_pain'
    ORAL_MEDICINE = 'oral_medicine'
    DENTAL_PUBLIC_HEALTH = 'dental_public_health'
    GENERAL_DENTISTRY = 'general_dentistry'
    COSMETIC_DENTISTRY = 'cosmetic_dentistry'
    RESTORATIVE_DENTISTRY = 'restorative_dentistry'
    GERIATRIC_DENTISTRY = 'geriatric_dentistry'
    DENTAL_HYGIENIST = 'dental_hygienist'
    DENTAL_ASSISTANT = 'dental_assistant'
    
    CHOICES_SPECIALITY = (
        (ENDODONTIST, 'Endodontist'),
        (ORTHODONTIST, 'Orthodontist'),
        (PERIODONTIST, 'Periodontist'),
        (PROSTHODONTIST, 'Prosthodontist'),
        (MAXILLOFACIAL_SURGEON, 'Maxillofacial Surgeon'),
        (MAXILLOFACIAL_RADIOLOGIST, 'Maxillofacial Radiologist'),
        (ANESTHESIOLOGISTS, 'Anesthesiologists'),
        (MAXILLOFACIAL_PATHOLOGIST, 'Maxillofacial Pathologist'),
        (PEDIATRIC_DENTIST, 'Pediatric Dentist'),
        (OROFACIAL_PAIN, 'Orofacial Pain'),
        (ORAL_MEDICINE, 'Oral Medicine'),
        (DENTAL_PUBLIC_HEALTH, 'Dental Public Health'),
        (GENERAL_DENTISTRY, 'General Dentistry'),
        (COSMETIC_DENTISTRY, 'Cosmetic Dentistry'),
        (RESTORATIVE_DENTISTRY, 'Restorative Dentistry'),
        (GERIATRIC_DENTISTRY, 'Geriatric dentistry'),
        (DENTAL_HYGIENIST, 'Dental Hygienist'),
        (DENTAL_ASSISTANT, 'Dental Assistant'),
    )
    speciality = models.CharField(max_length=30, choices=CHOICES_SPECIALITY, default=GENERAL_DENTISTRY)
    created_by = models.ForeignKey(User, related_name='dentists', on_delete=models.CASCADE)
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
