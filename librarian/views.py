from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from .forms import CreateBorrowing, CreateBorrower, CreateBook, CreateCd, CreateDvd
from .models import Book, Dvd, Cd, BoardGame, Borrowing, Media
from borrower.models import Borrower

import logging

logging.basicConfig(filename="logfile.log",
                    format='%(asctime)s-%(levelname)s-%(message)s',
                    datefmt='%d-%b-%y%H:%M:%S')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def home(request):
    return render(request, 'librarian/home.html')


@login_required
def index(request):
    return render(request, 'librarian/index.html')


@login_required
def create_media_choice(request):
    return render(request, 'librarian/create_media_choice.html')


@login_required
def create_borrower(request):
    return render(request, 'librarian/create_borrower.html')


@login_required
def medias_list(request):
    books = Book.objects.all()
    dvds = Dvd.objects.all()
    cds = Cd.objects.all()
    boardgames = BoardGame.objects.all()
    borrowings = Borrowing.objects.all()
    return render(request,
                  'librarian/medias_list.html',
                  {'books': books, 'dvds': dvds, 'cds': cds, 'boardgames': boardgames, 'borrowings': borrowings})


class CreateBook(LoginRequiredMixin, CreateView):
    model = Book
    form_class = CreateBook
    template_name = 'librarian/create_book.html'

    def get_success_url(self):
        return reverse_lazy("medias_list")


class CreateDvd(LoginRequiredMixin, CreateView):
    model = Dvd
    form_class = CreateDvd
    template_name = 'librarian/create_dvd.html'

    def get_success_url(self):
        return reverse_lazy("medias_list")


class CreateCd(LoginRequiredMixin, CreateView):
    model = Cd
    form_class = CreateCd
    template_name = 'librarian/create_cd.html'

    def get_success_url(self):
        return reverse_lazy("medias_list")


def create_borrowing(request, name):
    media = Media.objects.get(name=name)
    borrowing = Borrowing()
    if request.method == 'POST':
        form = CreateBorrowing(request.POST)
        if form.is_valid():
            borrowing.media = media
            borrowing.borrower = form.cleaned_data['borrower']
            media.borrower = form.cleaned_data['borrower']
            media.availability = False
            borrowing.save()
            media.save()
            return redirect('medias_list')
    else:
        form = CreateBorrowing()
    return render(request, 'librarian/create_borrowing.html',
                  {'form': form})


def delete_borrowing(request, name):
    media = Media.objects.get(name=name)
    borrowing = Borrowing.objects.get(media=media)
    borrowing.delete()
    media.availability = True
    media.save()
    media.borrower.delete()
    return redirect('medias_list')


class CreateBorrower(LoginRequiredMixin, CreateView):
    model = Borrower
    form_class = CreateBorrower
    template_name = "librarian/create_borrower.html"

    def get_success_url(self):
        return reverse_lazy('borrowers_list')


class UpdateBorrower(LoginRequiredMixin, UpdateView):
    model = Borrower
    form_class = CreateBorrower
    template_name = "librarian/create_borrower.html"

    def get_success_url(self):
        return reverse_lazy("detail_borrower", kwargs={"pk": self.object.name})


class DeleteBorrower(LoginRequiredMixin, DeleteView,):
    model = Borrower

    def get_success_url(self):
        return reverse_lazy("borrowers_list")
