from django.db import models


class Borrower(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name="Emprunteur")

    def __str__(self):
        return self.name


