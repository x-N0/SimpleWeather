from django.forms import ModelForm, TextInput
from .models import Location


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['name']
        widgets = {'name': TextInput(attrs={'class': 'input', 'placeholder': 'Location'})}
