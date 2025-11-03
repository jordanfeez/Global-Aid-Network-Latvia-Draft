from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
import re


class CheckForCustomCharacters:
    def validate(self, password, user=None):

       pattern = r'[!@#$%^&*()_\-+={}[\]|:;\'",.<>?/]' 
       if not re.search(pattern, password):
            raise ValidationError(_("You must have at least one special character in your password."))
        
    def get_help_text(self):
       return _("Your password must contain at least one special character.")