from django.shortcuts import render

from .forms import CreateCd, CreateDvd, CreateBook
from .models import Book, Dvd, Cd, BoardGame


def index(request):
    return render(request, 'librarian/index.html')


def createmedia(request):
    return render(request, 'librarian/create_media.html')


def mediaslist(request):
    books = Book.objects.all()
    dvds = Dvd.objects.all()
    cds = Cd.objects.all()
    return render(request, 'librarian/lists.html')


def addbook(request):
    if request.method == 'POST':
        createbook = CreateBook(request.POST)
        if createbook.is_valid():
            book = Book()
            book.name = createbook.cleaned_data['name']
            book.author = createbook.cleaned_data['author']
            book.save()
            books = Book.objects.all()
            return render(request,
                          'librarian/lists.html',
                          {'books': books})

    else:
        createbook = CreateBook()
        return render(request,
                      'librarian/create_book.html',
                      {'createBook': createbook})


def adddvd(request):
    if request.method == 'post':
        createdvd = CreateDvd(request.POST)
        if createdvd.is_valid():
            dvd = Dvd()
            dvd.name = createdvd.cleaned_data['name']
            dvd.director = createdvd.cleaned_data['director']
            dvd.save()
            dvds = dvd.objects.all()
            return render(request,
                          'librarian/create_dvd.html',
                          {'dvds': dvds})
    else:
        createdvd = CreateDvd()
        return render(request,
                      'librarian/create_dvd.html',
                      {'createDvd': createdvd})


def addcd(request):
    if request.method == 'post':
        createcd = CreateCd(request.POST)
        if createcd.is_valid():
            cd = Cd()
            cd.name = CreateCd.cleaned_data['name']
            cd.director = CreateCd.cleaned_data['director']
            cd.save()
            cd = cd.objects.all()
            return render(request,
                          'librarian/create_cd.html',
                          {'createCd': createcd})
    else:
        createcd = CreateCd()
        return render(request,
                      'librarian/create_cd.html',
                      {'createCd': createcd})
