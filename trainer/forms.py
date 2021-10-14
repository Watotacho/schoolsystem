from django import forms

from .models import trainer
class TrainerRegistrationForm(forms.ModelForm):
    class Meta:
        model=trainer
        fields="__all__"
