# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, CreditCard


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number')
        help_texts = {
            'username': '',
            'email': '',
            'phone_number': '',
        }


class CreditCardForm(forms.ModelForm):
    class Meta:
        model = CreditCard
        fields = ['card_number', 'expiry_date', 'cvv']
        widgets = {
            'expiry_date': forms.TextInput(attrs={'placeholder': 'MM/YY'}),
            'cvv': forms.PasswordInput(),
        }