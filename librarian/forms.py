from django import forms


class CreateBook(forms.Form):
    name = forms.CharField(required=True, label="Nom")
    author = forms.CharField(required=True, label="Auteur")


class CreateDvd(forms.Form):
    name = forms.CharField(required=True, label="Nom")
    producer = forms.CharField(required=True, label='Réalisateur')


class CreateCd(forms.Form):
    name = forms.CharField(required=True, label="Nom")
    entertainer = forms.CharField(required=True, label="artiste")

