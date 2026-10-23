from django import forms
from .models import AssistanceRequest

class AssistanceRequestForm(forms.Form):
    category = forms.ChoiceField(choices=AssistanceRequest.Category.choices)
    text = forms.CharField(min_length=1, max_length=5000, strip=True)
