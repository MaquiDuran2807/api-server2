from django.forms import ModelForm
from .models import Driver

class DriverForm(ModelForm):
    """Form definition for Client."""

    class Meta:
        """Meta definition for Clientform."""

        model = Driver
        fields = ('__all__')
