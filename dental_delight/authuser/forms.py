from allauth.account.forms import SignupForm, password_validation, PasswordField, LoginForm
from django import forms
from django.utils.translation import gettext_lazy as _
 
class UserSignupForm(SignupForm):
    template_name = 'authuser/forms/signup_form.html'
    email = forms.EmailField(
        label=_("Email"),
        required=True,
        widget=forms.TextInput(
            attrs={"type": "email", "placeholder": _("someaddress@domain.com")}
        ),
    )
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"] = forms.CharField(
            label=_("Password"),
            help_text=password_validation.password_validators_help_text_html(),
            widget=forms.PasswordInput(
                attrs={ "placeholder": _("•••••••••••") }
            )
        )
        self.fields["password2"] = forms.CharField(
            label=_("Confirm Password"),
            widget=forms.PasswordInput(
                attrs={ "placeholder": _("•••••••••••") }
            )
        )

    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

class UserLoginForm(LoginForm):
    template_name = 'authuser/forms/login_form.html'
    password = forms.CharField(
        label=_("Password"),
        help_text=password_validation.password_validators_help_text_html(),
        widget=forms.PasswordInput(
            attrs={ "placeholder": _("•••••••••••") }
        )
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        login_widget = forms.EmailInput(
                attrs={
                    "placeholder": _("someaddress@domain.com"),
                    "autocomplete": "email",
                }
            )
        self.fields["login"] = login_field = forms.EmailField(label=_("Email"), widget=login_widget)