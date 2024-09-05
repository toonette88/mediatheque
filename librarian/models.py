from django.db import models
from borrower.models import Borrower


class Media(models.Model):
    name = models.fields.CharField(max_length=150)
    borrowingDate = models.fields.DateField(null=True, blank=True)
    availability = models.fields.BooleanField(default="True")
    borrower = models.ForeignKey(Borrower, on_delete=models.SET_NULL, null=True, blank=True)


class Book(Media):
    author = models.fields.CharField(max_length=150)


class Dvd(Media):
    producer = models.fields.CharField(max_length=150)


class Cd(Media):
    entertainer = models.fields.CharField(max_length=150)


class BoardGame (models.Model):
    name = models.fields.CharField(max_length=150)
    creator = models.fields.CharField(max_length=150)





