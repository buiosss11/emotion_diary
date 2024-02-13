from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "username": forms.TextInput(
                ),
            "password": forms.TextInput(
                attrs={
                    "type": "password", 
                    }
            )
        }
class CreateUserForm(forms.ModelForm):
    class Meta :
        model = User
        fields = ["username","password","email","last_name","first_name"]
        widgets = {
            "username":forms.TextInput(),
            "password":forms.TextInput(attrs={"type":"password"}),
            "email":forms.TextInput(),
            "last_name":forms.TextInput(),
            "first_name":forms.TextInput(),
        }



class EditUserForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']