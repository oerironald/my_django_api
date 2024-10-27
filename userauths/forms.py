from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User, Profile

class UserRegisterForm(UserCreationForm):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': "Enter Full Name",
            'class': "form-control"
        }),
        label="Full Name"
    )
    
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': "Username",
            'class': "form-control"
        }),
        label="Username"
    )
    
    email = forms.EmailField(
        widget=forms.TextInput(attrs={
            'placeholder': "Email Address",
            'class': "form-control"
        }),
        label="Email"
    )
    
    phone = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': "Phone Number",
            'class': "form-control"
        }),
        label="Phone"
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': "Password",
            'class': "form-control"
        }),
        label="Password"
    )
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': "Confirm Password",
            'class': "form-control"
        }),
        label="Confirm Password"
    )

    class Meta:
        model = User
        fields = ['full_name', 'username', 'email', 'phone', 'password1', 'password2']