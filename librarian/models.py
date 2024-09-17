from django.db import models

from borrower.models import Borrower


class Media(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Titre", primary_key=True)
    availability = models.BooleanField(default="True")
    borrower = models.ForeignKey(Borrower, null=True, blank=True, on_delete=models.SET_NULL, related_name='Media')

    def __str__(self):
        return self.name


class Book(Media):
    author = models.CharField(max_length=50)


class Dvd(Media):
    producer = models.CharField(max_length=50)


class Cd(Media):
    entertainer = models.CharField(max_length=50)


class Borrowing(models.Model):
    media = models.ForeignKey(Media, on_delete=models.DO_NOTHING)
    borrower = models.ForeignKey(Borrower, on_delete=models.DO_NOTHING)
    borrowingDate = models.DateTimeField(auto_now_add=True)


class BoardGame (models.Model):
    name = models.CharField(max_length=50)
    creator = models.CharField(max_length=50)

    def __str__(self):
        return self.name
