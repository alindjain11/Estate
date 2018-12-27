from .models import Showall

from django import forms

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Showall
        exclude = ('seller','list_date',)
