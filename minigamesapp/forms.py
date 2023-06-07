from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm




class UserRegistrationForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "placeholder":"Enter username",
    }),label="Username")

    email=forms.CharField(widget=forms.TextInput(attrs={
        "class":"input",
        "type":"email",
        "placeholder":"Enter your Email Address",
    }),label="Email")

    password1=forms.CharField(widget=forms.TextInput(attrs={
        "class":"input",
        "type":"password",
        "placeholder":"Enter Password",
    }),label="Password")

    password2=forms.CharField(widget=forms.TextInput(attrs={
        "class":"input",
        "type":"password",
        "placeholder":"Confirm your Password",
    }),label="Confirm Password")
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        
class loginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "placeholder":"Enter username",
    }),label="Username")

    password=forms.CharField(widget=forms.TextInput(attrs={
        "class":"input",
        "type":"password",
        "placeholder":"Enter Password",
    }),label="Password")

