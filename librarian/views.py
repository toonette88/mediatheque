from django.http import HttpResponse

def index(request):
    return HttpResponse("Bonjour, bienvenue dans l'application bibliothécaire")
# Create your views here.
