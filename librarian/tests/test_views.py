import pytest

from django.urls import reverse
from django.test import Client
from borrower.models import Borrower
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_borrower_detail_view():
    client = Client()
    Borrower.objects.create(name = 'Toto Test')
    path = reverse('borrower_detail', kwargs={'pk': 1})
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<p>Toto Test</p>"

    assert content == expected_content
    assert response.status_code == 200
    assertTemplateUsed(response, "borrower_detail.html")
