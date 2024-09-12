from django.db import models
from django.utils import timezone

from borrower.models import Borrower


class Media(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Titre")
    availability = models.BooleanField(default="True")

    def __str__(self):
        return self.name


class Book(Media):
    author = models.CharField(max_length=50)


class Dvd(Media):
    producer = models.CharField(max_length=50)


class Cd(Media):
    entertainer = models.CharField(max_length=50)


class Borrowing(models.Model):
    media = models.ForeignKey(Book,
                              on_delete=models.PROTECT,
                              null=True, blank=True,
                              default="")
    borrower = models.ForeignKey(Borrower, on_delete=models.PROTECT, default="", null=True, blank=True)
    borrowingDate = models.DateField(default=timezone.now)


def __str__(self):
    return f"{self.get_media_display()}{self.nom}"


class BoardGame (models.Model):
    name = models.CharField(max_length=50)
    creator = models.CharField(max_length=50)

    def __str__(self):
        return self.name
