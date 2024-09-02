from django.http import HttpResponse
from django.template import loader

from .forms import CreateCd, CreateDvd, CreateBook
from .models import Media, Book, Dvd, Cd, BoardGame


def index(request):
    menu = print("Bienvenu")
    template = loader.get_template("librarian/index.html")
    context = {"menu": menu, }
    return HttpResponse(template.render(context, request))


