from django.db import models
from borrower.models import Borrower


class Media(models.Model):
    name = models.CharField(max_length=50)
    borrowingDate = models.DateField(null=True, blank=True)
    availability = models.BooleanField(default="True")
    borrower = models.ForeignKey(Borrower, on_delete=models.SET_DEFAULT, null=True, blank=True, default="")

    def __str__(self):
        return self.name


class Book(Media):
    author = models.CharField(max_length=50)


class Dvd(Media):
    producer = models.CharField(max_length=50)


class Cd(Media):
    entertainer = models.CharField(max_length=50)


class BoardGame (models.Model):
    name = models.CharField(max_length=50)
    creator = models.CharField(max_length=50)

    def __str__(self):
        return self.name





