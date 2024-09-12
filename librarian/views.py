from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from dal import autocomplete
from .forms import CreateCd, CreateDvd, CreateBook, CreateBorrowing, CreateBorrower, UpdateBorrower
from .models import Book, Dvd, Cd, BoardGame, Borrowing, Media
from borrower.models import Borrower


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
    borrowing = Borrowing.objects.all()
    return render(request,
                  'librarian/medias_list.html',
                  {'books': books, 'dvds': dvds, 'cds': cds, 'boardgames': boardgames})


class CreateBook(CreateView, LoginRequiredMixin):
    model = Book
    template_name = 'librarian/create_book.html'

    def get_success_url(self):
        return reverse_lazy("librarian/medias_list.html")


class CreateDvd(CreateView, LoginRequiredMixin):
    model = Dvd
    template_name = 'librarian/create_dvd.html'

    def get_success_url(self):
        return reverse_lazy("librarian/medias_list.html")


class CreateCd(CreateView, LoginRequiredMixin):
    model = Cd
    template_name = 'librarian/create_cd.html'

    def get_success_url(self):
        return reverse_lazy("librarian/medias_list.html")


class CreateBorrowing(CreateView, LoginRequiredMixin):
    model = Borrowing
    form_class = CreateBorrowing
    template_name = 'librarian/create_borrowing.html'

    def get_success_url(self):
        return reverse_lazy("librarian/medias_list.html", kwargs={"pk": self.objects.id})


class CreateBorrower(CreateView, LoginRequiredMixin):
    model = Borrower
    form_class = CreateBorrower
    template_name = "librarian/create_borrower.html"

    def get_success_url(self):
        return reverse_lazy("detail_borrower", kwargs={"pk": self.object.id})


class UpdateBorrower(UpdateView, LoginRequiredMixin):
    model = Borrower
    form_class = CreateBorrower
    template_name = "librarian/create_borrower.html"

    def get_success_url(self):
        return reverse_lazy("detail_borrower", kwargs={"pk": self.object.id})


class BorrowerAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Borrower.objects.none()
        qs = Borrower.objects.all()
        if self.q:
            qs = qs.filter(name_istartswith=self.q)
        return qs


class DeleteBorrower(DeleteView, LoginRequiredMixin):
    model = Borrower

    def get_success_url(self):
        return reverse_lazy("borrowers_list")
