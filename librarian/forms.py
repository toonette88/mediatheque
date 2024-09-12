from django.forms import ModelForm
from dal import autocomplete
from django.core.exceptions import ValidationError

from borrower.models import Borrower
from librarian.models import Book, Dvd, Cd, Borrowing


class CreateBook(ModelForm):
    class Meta:
        model = Book
        fields = ("name", "author")

class CreateDvd(ModelForm):
    class Meta:
        model = Dvd
        fields = ("name", "producer")


class CreateCd(ModelForm):
    class Meta:
        model = Cd
        fields = ("name", "entertainer")


class UpdateBorrower(ModelForm):
    class Meta:
        model = Borrower
        fields = ['name']


class CreateBorrowing(ModelForm):
    class Meta:
        model = Borrowing
        fields = ('borrower',)
        widgets = {
            'borrower': autocomplete.ModelSelect2(url='borrower_autocomplete')
        }


class CreateBorrower(ModelForm):
    class Meta:
        model = Borrower
        fields = ['name']
