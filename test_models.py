from django.test import TestCase
from django.contrib.auth.models import User
from librarian.models import Book, Borrowing
from borrower.models import Borrower


class BookModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='toto', password="1234")
        self.borrower = Borrower.objects.create(name="totobis")
        self.book = Book.objects.create(name='One book', author='Author')

    def test_book_creation(self):
        self.assertEqual(self.book.name, 'One book')
        self.assertEqual(self.book.author, 'Author')
        self.assertTrue(self.book.availability)

    def test_borrowing_creation(self):
        borrowing = Borrowing.objects.create(media=self.book, borrower=self.borrower)
        self.assertEqual(self.media.name)
        self.assertEqual(self.borrower.borrower.name, 'totobis')

    def test_borrower_creation(self):
        self.assertEqual(self.borrower.borrower.name, 'totobis')

