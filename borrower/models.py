from django.db import models


class Borrower(models.Model):
    name = models.fields.CharField(max_length=150)

