from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Appointment
from django.utils.translation import gettext_lazy as _

class AddAppointmentForm(forms.ModelForm):
    date = forms.DateField(
        label=_('Date'),
        widget=forms.DateInput(
            attrs={"type": "text", "placeholder": _("Select date"), "datepicker-format": "mm/dd/yyyy" }
        )
    )
        
    class Meta:
        model = Appointment
        fields = ["date", "time", "description", "dentists" ]