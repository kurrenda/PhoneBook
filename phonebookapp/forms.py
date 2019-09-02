from django import forms
from .models import Email, Telefon, Osoba

class OsobaForm(forms.ModelForm):
    class Meta:
        model = Osoba
        fields = ['imie','nazwisko']

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['email']


class TelefonForm(forms.ModelForm):
    class Meta:
        model = Telefon
        fields = ['telefon']