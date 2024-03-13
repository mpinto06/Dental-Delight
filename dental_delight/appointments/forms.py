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
            attrs={"type": "date", "placeholder": _("Select date"), "datepicker-format": "mm/dd/yyyy" }
        )
    )

    time = forms.TimeField(
        label=('Time'),
        widget=forms.TimeInput(
            attrs={"type": "time", "placeholder": _("Select time") }
        )
    )
        
    class Meta:
        model = Appointment
        fields = ["date", "time", "description", "dentists" ]