from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    LIBRARIAN = 'LIBRARIAN'
    BORROWER = 'BORROWER'

    ROLE_CHOICES = (
        (LIBRARIAN, 'Bibliothécaire'),
        (BORROWER, 'Membre')
    )

    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')
