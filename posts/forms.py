from typing import Any
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "nicknames"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "formControlInput",
                    "placeholder": "제목",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "id": "exampleFormControlTextarea1",
                    "placeholder": "내용을 입력하세요.",
                }
            ),
            "nicknames": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "formControlInput",
                    "placeholder": "이름 입력",
                }
            ),
        }
