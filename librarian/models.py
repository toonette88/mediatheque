from django.db import models

from borrower.models import Borrower


class Media(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Titre", primary_key=True)
    availability = models.BooleanField(default="True", verbose_name="Disponibilité")
    borrower = models.ForeignKey(Borrower, null=True, blank=True,
                                 on_delete=models.SET_NULL,
                                 related_name='Media', verbose_name="Emprunteur")

    def __str__(self):
        return self.name


class Book(Media):
    author = models.CharField(max_length=50, verbose_name="Auteur")


class Dvd(Media):
    producer = models.CharField(max_length=50, verbose_name="Réalisateur")


class Cd(Media):
    entertainer = models.CharField(max_length=50, verbose_name="Artiste")


class Borrowing(models.Model):
    media = models.ForeignKey(Media, on_delete=models.DO_NOTHING, verbose_name="Media")
    borrower = models.ForeignKey(Borrower, on_delete=models.DO_NOTHING, verbose_name="Emprunteur")
    borrowingDate = models.DateTimeField(auto_now_add=True, verbose_name="Date d'emprunt")

    def __str__(self):
        return f"{self.borrower.name} a emprunté {self.media.name}"


class BoardGame (models.Model):
    name = models.CharField(max_length=50, verbose_name="Titre")
    creator = models.CharField(max_length=50, verbose_name="Créateur")

    def __str__(self):
        return self.name
