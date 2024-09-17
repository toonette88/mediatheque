from django.forms import ModelForm
from django.core.exceptions import ValidationError


from borrower.models import Borrower
from librarian.models import Book, Dvd, Cd, Borrowing


class CreateBook(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author']


class CreateDvd(ModelForm):
    class Meta:
        model = Dvd
        fields = ['name', 'producer']


class CreateCd(ModelForm):
    class Meta:
        model = Cd
        fields = ['name', 'entertainer']


class CreateBorrowing(ModelForm):
    class Meta:
        model = Borrowing
        fields = ['borrower']


class CreateBorrower(ModelForm):
    class Meta:
        model = Borrower
        fields = '__all__'


class UpdateBorrower(ModelForm):
    class Meta:
        model = Borrower
        fields = '__all__'
        label = {'Nom Prénom'}
