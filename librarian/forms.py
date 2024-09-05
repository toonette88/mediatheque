from django import forms


class CreateBook(forms.Form):
    name = forms.CharField(label="Nom")
    author = forms.CharField(label="Auteur")


class CreateDvd(forms.Form):
    name = forms.CharField(label="Nom")
    producer = forms.CharField(label='Réalisateur')


class CreateCd(forms.Form):
    name = forms.CharField(label="Nom")
    entertainer = forms.CharField(label="Artiste")


class UpdateBorrower(forms.Form):
    name = forms.CharField(label="Nom")


class CreateBorrowing(forms.Form):
    borrower = forms.CharField(label="Emprunteur")
    borrowingDate = forms.DateField(label="Date d'emprunt")


class CreateBorrower(forms.Form):
    name = forms.CharField(label="nom")