from django.forms import ModelForm
from .models import Client

class ClientForm(ModelForm):
    """Form definition for Client."""

    class Meta:
        """Meta definition for Clientform."""

        model = Client
        fields = ('__all__')
