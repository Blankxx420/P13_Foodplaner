from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserRegistrationForm(UserCreationForm):
    """Customize form that create User"""
    email = forms.EmailField(max_length=254, help_text="Obligatoire")
    username = forms.CharField(max_length=60, help_text="Obligatoire")

    class Meta:
        model = User
        fields = ["email", "username", "phone_number", "password1", "password2"]


class UserUpdateForm(forms.ModelForm):
    """customize form for updating user information"""
    email = forms.EmailField(initial=None, max_length=254)
    username = forms.CharField(initial=None, max_length=254)
    phone_number = forms.CharField(initial=None, max_length=12)

    class Meta:
        model = User
        fields = ["email", "username", "phone_number"]