from django import forms
from django.core.exceptions import ValidationError

from borrower.models import Borrower
from librarian.models import Media


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
    name = forms.CharField(label="Nom",
                           required=True,)

    class Meta:
        model = Borrower
        fields = ['name']


class CreateBorrowing(forms.ModelForm):
    class Meta:
        model = Media
        fields = (
            "borrower",
            "borrowingDate",
        )
        labels = {
            'borrower' : 'Emprunteur',
            'borrowingDate' : "Date d'emprunt"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['borrowingDate'].widget.attrs['class'] = 'datePicker'

    def clean(self):
        cleaned_data = super().clean()
        borrower_name = cleaned_data.get('borrower')

        try:
            borrower = Borrower.objects.get(name=borrower_name)
        except Borrower.DoesNotExist:
            raise ValidationError(f"Emprunteur {borrower_name} n'existe pas.")


class CreateBorrower(forms.Form):
    name = forms.CharField(label="Nom Prénom ")