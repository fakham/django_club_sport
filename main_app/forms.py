from . import models
from django import forms


class AdherentForm(forms.ModelForm):
    class Meta:
        model = models.Adherent
        fields = ['prenom', 'nom', 'username', 'email', 'password', 'adresse', 'genre', 'tel']
