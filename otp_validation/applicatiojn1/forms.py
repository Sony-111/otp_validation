from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class RegistrationForm(UserCreationForm):
    email=forms.CharField(widget=forms.EmailInput(attrs={"placeholder":"Enter Email Address", "class":"form-control"}))
    username=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter Username","class":"form-control"}))
    password1=forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"placeholder":"Enter password","class":"form-control"}))
    password2=forms.CharField(label="Confrim Password", widget=forms.PasswordInput(attrs={"placeholder":"Enter password","class":"form-control"}))

    class Meta:
        model=get_user_model()
        fields=["email","username","password1","password2"]