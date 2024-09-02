from django.db import models


class Media(models.Model):
    name = models.fields.CharField(max_length=150)
    borrowingDate = models.fields.DateField
    availability = models.fields.BooleanField(default="")
    borrower = models.fields.CharField(max_length=150, default="")


class Book(Media):
    author = models.fields.CharField(max_length=150)


class Dvd(Media):
    producer = models.fields.CharField(max_length=150)


class Cd(Media):
    entertainer = models.fields.CharField(max_length=150)


class BoardGame (models.Model):
    name = models.fields.CharField(max_length=150)
    creator = models.fields.CharField(max_length=150)


