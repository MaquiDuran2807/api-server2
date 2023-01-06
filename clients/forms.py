from django.forms import ModelForm
from django import forms
from .models import Client

class ClientForm(ModelForm):
    """Form definition for Client."""

    class Meta:
        """Meta definition for Clientform."""

        model = Client
        fields = ('identification','name','lastname','genero','email','img','tel')
        #agregar clases de bootstrap a los campos
        widgets = { 
            'identification': forms.TextInput(attrs={'class':'form-control '}),
            'name': forms.TextInput(attrs={'class':'form-control '}),
            'lastname': forms.TextInput(attrs={'class':'form-control '}),
            'genero': forms.Select(attrs={'class':'form-control  '}),
            'email': forms.EmailInput(attrs={'class':'form-control '}),
            'img': forms.FileInput(attrs={'class':'form-control '}),
            'tel': forms.TextInput(attrs={'class':'form-control '}),
        }

