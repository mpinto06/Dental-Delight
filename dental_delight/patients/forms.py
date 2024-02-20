from django import forms
from .models import Patient
from django.utils.translation import gettext_lazy as _

class AddPatientForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=30, 
        label=_('First Name'),
        widget=forms.TextInput(
            attrs={"type": "text", "placeholder": _("Leo") }
        )
    )
    last_name = forms.CharField(
        max_length=30, 
        label=_('Last Name'),
        widget=forms.TextInput(
            attrs={"type": "text", "placeholder": _("Messi") }
        )
    )
    email = forms.EmailField(
        label=_("Email"),
        required=True,
        widget=forms.TextInput(
            attrs={"type": "email", "placeholder": _("someaddress@domain.com")}
        ),
    )
    phone_number = forms.CharField(
        max_length=30, 
        label=_('Phone Number'),
        widget=forms.TextInput(
            attrs={"type": "text", "placeholder": _("(555) 555-1234") }
        )
    )
    citizen_number = forms.CharField(
        max_length=30, 
        label=_('Citizen Number'),
        widget=forms.TextInput(
            attrs={"type": "text", "placeholder": _("123456789") }
        )
    )

    class Meta:
        model = Patient
        fields = ["first_name", "last_name", "email", "phone_number", "citizen_number"]