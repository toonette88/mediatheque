from django.shortcuts import render

from .forms import CreateCd, CreateDvd, CreateBook, CreateBorrowing, CreateBorrower
from .models import Book, Dvd, Cd, BoardGame, Media
from borrower.models import Borrower


def index(request):
    return render(request, 'librarian/index.html')


def create_media(request):
    return render(request, 'librarian/create_media.html')


def create_borrower(request):
    return render(request, 'librarian/create_borrower.html')


def medias_list(request):
    books = Book.objects.all()
    dvds = Dvd.objects.all()
    cds = Cd.objects.all()
    boardgames = BoardGame.objects.all()
    return render(request,
                  'librarian/medias_list.html',
                  {'books': books, 'dvds': dvds, 'cds': cds, 'boardgames': boardgames})


def add_book(request):
    if request.method == 'POST':
        create_book = CreateBook(request.POST)
        if create_book.is_valid():
            book = Book()
            book.name = create_book.cleaned_data['name']
            book.author = create_book.cleaned_data['author']
            book.save()
            books = Book.objects.all()
            dvds = Dvd.objects.all()
            cds = Cd.objects.all()
            boardgames = BoardGame.objects.all()
            return render(request,
                          'librarian/medias_list.html',
                          {'books': books, 'dvds': dvds, 'cds': cds, 'boardgames': boardgames})

    else:
        create_book = CreateBook()
        return render(request,
                      'librarian/create_book.html',
                      {'createBook': create_book})


def add_dvd(request):
    if request.method == 'POST':
        create_dvd = CreateDvd(request.POST)
        if create_dvd.is_valid():
            dvd = Dvd()
            dvd.name = create_dvd.cleaned_data['name']
            dvd.producer = create_dvd.cleaned_data['producer']
            dvd.save()
            books = Book.objects.all()
            dvds = Dvd.objects.all()
            cds = Cd.objects.all()
            boardgames = BoardGame.objects.all()
            return render(request,
                          'librarian/medias_list.html',
                          {'books': books, 'dvds': dvds, 'cds': cds, 'boardgames': boardgames})
    else:
        create_dvd = CreateDvd()
        return render(request,
                      'librarian/create_dvd.html',
                      {'createDvd': create_dvd})


def add_cd(request):
    if request.method == 'POST':
        create_cd = CreateCd(request.POST)
        if create_cd.is_valid():
            cd = Cd()
            cd.name = create_cd.cleaned_data['name']
            cd.entertainer = create_cd.cleaned_data['entertainer']
            cd.save()
            books = Book.objects.all()
            dvds = Dvd.objects.all()
            cds = Cd.objects.all()
            boardgames = BoardGame.objects.all()
            return render(request,
                          'librarian/medias_list.html',
                          {'books': books, 'dvds': dvds, 'cds': cds, 'boardgames': boardgames})
    else:
        create_cd = CreateCd()
        return render(request,
                      'librarian/create_cd.html',
                      {'createCd': create_cd})


def add_borrowing_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        create_borrowing = CreateBorrowing(request.POST)
        if create_borrowing.is_valid():
            book.borrower = create_borrowing.cleaned_data['borrower']
            book.borrowingDate = create_borrowing.cleaned_data['borrowingDate']
            book.availability = False
            book.save()
            books = Book.objects.all()
            return render(request,
                          'librarian/medias_list.html',
                          {'books': books})
    else:
        create_borrowing = CreateBorrowing(request.POST)
        return render(request,
                      'librarian/create_borrowing.html',
                      {'createBorrowing': create_borrowing})


def add_borrowing_dvd(request, id):
    dvd = Dvd.objects.get(id=id)
    if request.method == 'POST':
        create_borrowing = CreateBorrowing(request.POST)
        if create_borrowing.is_valid():
            dvd.borrower = create_borrowing.cleaned_data['borrower']
            dvd.borrowingDate = create_borrowing.cleaned_data['borrowingDate']
            dvd.availability = False
            dvd.save()
            dvds = Dvd.objects.all()
            return render(request,
                          'librarian/medias_list.html',
                          {'dvds': dvds})
    else:
        create_borrowing = CreateBorrowing(request.POST)
        return render(request,
                      'librarian/create_borrowing.html',
                      {'createBorrowing': create_borrowing})


def add_borrowing_cd(request, id):
        cd = Cd.objects.get(id=id)
        if request.method == 'POST':
            create_borrowing = CreateBorrowing(request.POST)
            if create_borrowing.is_valid():
                cd.borrower = create_borrowing.cleaned_data['borrower']
                cd.borrowingDate = create_borrowing.cleaned_data['borrowingDate']
                cd.availability = False
                cd.save()
                cds = Cd.objects.all()
                return render(request,
                              'librarian/medias_list.html',
                              {'cds': cds})
        else:
            create_borrowing = CreateBorrowing(request.POST)
            return render(request,
                          'librarian/create_borrowing.html',
                          {'createBorrowing': create_borrowing})


def add_borrower(request):
    if request.method == 'POST':
        create_borrower = CreateBorrower(request.POST)
        if create_borrower.is_valid():
            borrower = Borrower()
            borrower.name = create_borrower.cleaned_data['name']
            borrower.save()
            borrowers = Borrower.objects.all()
            return render(request,
                          'borrowers_list.html',
                          {'borrowers': borrowers})
    else:
        create_borrower = CreateBorrower()
        return render(request,
                      'librarian/create_borrower.html',
                      {'createBorrower': CreateBorrower})


