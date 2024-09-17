import pytest

from django.urls import reverse, resolve
from borrower.models import Borrower


@pytest.mark.django_db
def test_borrower_details_url():
    Borrower.objects.create( name = 'Test Toto')
    path = reverse('detail_borrower', kwargs={'pk': 1})

    assert path == " /1"
    assert resolve(path).view_name == 'detail_borrower'
