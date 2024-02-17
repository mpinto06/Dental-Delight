from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class SpecialCharacterValidator:
    def validate(self, password, user=None):
        if not any(not c.isalnum() for c in password):
            raise ValidationError(
                _("This password must contain at least one special character")
            )
    def get_help_text(self):
        return _(
            "Your password must contain at least one special character"
        )