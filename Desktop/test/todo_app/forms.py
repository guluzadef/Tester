from django import forms
from .models import *


class Add(forms.ModelForm):
    class Meta:
        model=Team
        fields =['text']