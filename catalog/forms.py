from django import forms
from .models import PhoneSold
from django.contrib.auth.models import User


class BuyPhoneForm(forms.ModelForm):
    class Meta:
        model = PhoneSold
        fields = ('email', 'phonenumber', 'address',)


class SignupForm(forms.ModelForm):
    name = forms.CharField(required=True)
    fname = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)

    class Meta:
        model = User
        fields = ('email', 'name', 'fname', 'name', 'password')
