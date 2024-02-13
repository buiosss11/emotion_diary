from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widget = {
            "username": forms.TextInput(
                attrs={
                    'id':'user_id'
                    }
                ),
            "password": forms.TextInput(
                attrs={
                    "type": "password", 
                    "class": "teetetet"
                    }
            )
        }
