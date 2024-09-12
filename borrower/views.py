from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Borrower
from librarian.views import Book, Dvd, Cd, BoardGame


def borrower_index(request):
    books = Book.objects.all()
    dvds = Dvd.objects.all()
    cds = Cd.objects.all()
    boardgames = BoardGame.objects.all()
    return render(request,
                  'borrower/borrower_index.html',
                   {'books': books, 'dvds': dvds, 'cds': cds, 'boardgames': boardgames})


@login_required
def borrowers_list(request):
    borrowers = Borrower.objects.all()
    return render(request,
                  'borrower/borrowers_list.html',
                  {'borrowers': borrowers})


