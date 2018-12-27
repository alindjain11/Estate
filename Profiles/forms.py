from .models import Profile
from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={}),
        required=True, max_length=30
    )
    class Meta:
        model = Profile
        fields = ['username','email','first_name','last_name','password','is_seller','description', 'photo']

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        email = user.email
        try:
            validate_email(email)
        except ValidationError:
            forms.ValidationError('please write valid email address')
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())
