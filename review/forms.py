from django import forms
from .models import Chorus

class ChoursForm(forms.ModelForm):
    class Meta:
        model = Chorus
        fields = ['yourname','songname','part','review']