from django import forms
from .models import User


class UserSignupForm(forms.ModelForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "Enter you username"
        }),
        label="Username")
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={
            "placeholder": "Enter your email"
        }), required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            "placeholder": "Enter your password"
        }))

    class Meta:
        model = User
        fields = ('username','email', 'password')
        exclude = ('is_active', 'created_on', 'updated_on')