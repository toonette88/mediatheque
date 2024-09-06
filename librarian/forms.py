from django import forms

from django.contrib.auth.models import User
from borrower.models import Borrower


class CreateBook(forms.Form):
    name = forms.CharField(label="Nom")
    author = forms.CharField(label="Auteur")


class CreateDvd(forms.Form):
    name = forms.CharField(label="Nom")
    producer = forms.CharField(label='Réalisateur')


class CreateCd(forms.Form):
    name = forms.CharField(label="Nom")
    entertainer = forms.CharField(label="Artiste")


class UpdateBorrower(forms.ModelForm):
    name = forms.CharField(label="Nom Prénom ",
                           required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Borrower
        fields = ['name']


class CreateBorrowing(forms.Form):
    borrower = forms.CharField(label="Emprunteur")
    borrowingDate = forms.DateField(label="Date d'emprunt")


class CreateBorrower(forms.Form):
    name = forms.CharField(label="Nom Prénom ")