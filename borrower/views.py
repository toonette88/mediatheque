from django.shortcuts import render
from .models import Borrower


def borrowers_list(request):
    borrowers = Borrower.objects.all()
    return render(request,
                  'borrower/borrowers_list.html',
                  {'borrowers': borrowers})

