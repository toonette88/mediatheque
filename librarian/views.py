from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import CreateCd, CreateDvd, CreateBook, CreateBorrowing, CreateBorrower, UpdateBorrower
from .models import Book, Dvd, Cd, BoardGame
from borrower.models import Borrower


def home(request):
    return render(request, 'librarian/home.html')


@login_required
def index(request):
    return render(request, 'librarian/index.html')


@login_required
def create_media(request):
    return render(request, 'librarian/create_media.html')


@login_required
def create_borrower(request):
    return render(request, 'librarian/create_borrower.html')


@login_required
def medias_list(request):
    books = Book.objects.all()
    dvds = Dvd.objects.all()
    cds = Cd.objects.all()
    boardgames = BoardGame.objects.all()
    return render(request,
                  'librarian/medias_list.html',
                  {'books': books, 'dvds': dvds, 'cds': cds, 'boardgames': boardgames})


@login_required
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


@login_required
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


@login_required
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


@login_required
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
            dvds = Dvd.objects.all()
            cds = Cd.objects.all()
            boardgames = BoardGame.objects.all()
            return render(request,
                          'librarian/medias_list.html',
                          {'books': books, 'dvds': dvds, 'cds': cds, 'boardgames': boardgames})
    else:
        create_borrowing = CreateBorrowing(request.POST, instance=book)
        return render(request,
                      'librarian/create_borrowing.html',
                      {'createBorrowing': create_borrowing})


@login_required
def add_borrowing_dvd(request, id):
    dvd = Dvd.objects.get(id=id)
    if request.method == 'POST':
        create_borrowing = CreateBorrowing(request.POST)
        if create_borrowing.is_valid():
            dvd.borrower = create_borrowing.cleaned_data['borrower']
            dvd.borrowingDate = create_borrowing.cleaned_data['borrowingDate']
            dvd.availability = False
            dvd.save()
            books = Book.objects.all()
            dvds = Dvd.objects.all()
            cds = Cd.objects.all()
            boardgames = BoardGame.objects.all()
            return render(request,
                          'librarian/medias_list.html',
                          {'books': books, 'dvds': dvds, 'cds': cds, 'boardgames': boardgames})
    else:
        create_borrowing = CreateBorrowing(request.POST, instance=dvd)
        return render(request,
                      'librarian/create_borrowing.html',
                      {'createBorrowing': create_borrowing})


@login_required
def add_borrowing_cd(request, id):
        cd = Cd.objects.get(id=id)
        if request.method == 'POST':
            create_borrowing = CreateBorrowing(request.POST)
            if create_borrowing.is_valid():
                cd.borrower = create_borrowing.cleaned_data['borrower']
                cd.borrowingDate = create_borrowing.cleaned_data['borrowingDate']
                cd.availability = False
                cd.save()
                books = Book.objects.all()
                dvds = Dvd.objects.all()
                cds = Cd.objects.all()
                boardgames = BoardGame.objects.all()
                borrowers = Borrower.objects.all()
                return render(request,
                              'librarian/medias_list.html',
                              {'books': books, 'dvds': dvds, 'cds': cds, 'boardgames': boardgames})
        else:
            create_borrowing = CreateBorrowing(request.POST, instance=cd)
            borrowers = Borrower.objects.all()
            return render(request,
                          'librarian/create_borrowing.html',
                          {'createBorrowing': create_borrowing, 'borrowers': borrowers})


@login_required
def add_borrower(request):
    if request.method == 'POST':
        create_borrower = CreateBorrower(request.POST)
        if create_borrower.is_valid():
            borrower = Borrower()
            borrower.name = create_borrower.cleaned_data['name']
            borrower.save()
            borrowers = Borrower.objects.all()
            return render(request,
                          'borrower/borrowers_list.html',
                          {'borrowers': borrowers})
    else:
        create_borrower = CreateBorrower()
        return render(request,
                      'librarian/create_borrower.html',
                      {'createBorrower': create_borrower})


@login_required
def modification_borrower(request, id):
    borrower = Borrower.objects.get(id=id)
    if request.method == 'POST':
        update_borrower = UpdateBorrower(request.POST, instance=borrower)
        if update_borrower.is_valid():
            update_borrower.save()
            borrowers = Borrower.objects.all()
            return render(request,
                          'borrower/borrowers_list.html',
                          {'borrowers': borrowers})
    else:
        update_borrower = UpdateBorrower(instance=borrower)
        return render(request,
                      'librarian/update_borrower.html',
                      {'updateBorrower': update_borrower, 'borrower': borrower})


@login_required
def deletion_borrower(request, id):
    borrower = Borrower.objects.get(id=id)
    if request.method == 'POST':
        borrower.delete()
        borrowers = Borrower.objects.all()
        return render(request,
                      'borrower/borrowers_list.html',
                      {'borrowers': borrowers})
    else:
        books = Book.objects.all()
        dvds = Dvd.objects.all()
        cds = Cd.objects.all()
        boardgames = BoardGame.objects.all()
        return render(request,
                      'librarian/medias_list.html',
                      {'books': books, 'dvds': dvds, 'cds': cds, 'boardgames': boardgames})


@login_required
def deletion_borrowing_book(request, id):
    book = Book.objects.get(id=id)
    book.borrower = ""
    book.borrowingDate = "null"
    book.availability = True
    book.save()
    books = Book.objects.all()
    dvds = Dvd.objects.all()
    cds = Cd.objects.all()
    boardgames = BoardGame.objects.all()
    return render(request,
              'librarian/medias_list.html',
              {'books': books, 'dvds': dvds, 'cds': cds, 'boardgames': boardgames})

@login_required
def deletion_borrowing_dvd(request, id):
    dvd = Dvd.objects.get(id=id)
    if request.method == 'POST':
        dvd.borrower = ""
        dvd.borrowingDate = ""
        dvd.availability = True
        dvd.save()
        books = Book.objects.all()
        dvds = Dvd.objects.all()
        cds = Cd.objects.all()
        boardgames = BoardGame.objects.all()
        return render(request,
                      'librarian/medias_list.html',
                      {'books': books, 'dvds': dvds, 'cds': cds, 'boardgames': boardgames})
    else:
        books = Book.objects.all()
        dvds = Dvd.objects.all()
        cds = Cd.objects.all()
        boardgames = BoardGame.objects.all()
        return render(request,
                      'librarian/medias_list.html',
                      {'books': books, 'dvds': dvds, 'cds': cds, 'boardgames': boardgames})


@login_required
def deletion_borrowing_cd(request, id):
    cd = Cd.objects.get(id=id)
    if request.method == 'POST':
        cd.borrower = ""
        cd.borrowingDate = ""
        cd.availability = True
        cd.save()
        books = Book.objects.all()
        dvds = Dvd.objects.all()
        cds = Cd.objects.all()
        boardgames = BoardGame.objects.all()
        return render(request,
                      'librarian/medias_list.html',
                      {'books': books, 'dvds': dvds, 'cds': cds, 'boardgames': boardgames})
    else:
        books = Book.objects.all()
        dvds = Dvd.objects.all()
        cds = Cd.objects.all()
        boardgames = BoardGame.objects.all()
        return render(request,
                      'librarian/medias_list.html',
                      {'books': books, 'dvds': dvds, 'cds': cds, 'boardgames': boardgames})
