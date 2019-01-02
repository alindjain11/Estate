from .models import *

from django import forms

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Showall
        exclude = ('seller','list_date',)


class EnquiryForm(forms.ModelForm):

    from_email = forms.CharField(widget=forms.EmailInput(
    attrs={'class':'form-control','placeholder':'Email'}
    ),required=True, max_length=100)

    message = forms.CharField(widget=forms.EmailInput(
    attrs={'class':'form-control','placeholder':'enquiry message'}
    ),required=True, max_length=10000)

    dealer = forms.BooleanField(required=True)

    class Meta:
        model = Enquiry
        fields = ['from_email', 'message', 'dealer']
