from django.urls import path
from django.views.generic import DetailView

from borrower.models import Borrower
from librarian.views import (medias_list, create_media_choice, CreateBorrower, index, UpdateBorrower,
                             DeleteBorrower, create_borrowing, CreateCd, CreateDvd, CreateBook, delete_borrowing)

urlpatterns = [
    path("", index, name='index'),
    path("medias_list", medias_list, name='medias_list'),
    path('create_book', CreateBook.as_view(), name='create_book'),
    path('create_dvd', CreateDvd.as_view(), name='create_dvd'),
    path('create_cd', CreateCd.as_view(), name='create_cd'),
    path("create_media_choice", create_media_choice, name='create_media_choice'),
    path("create_borrower", CreateBorrower.as_view(), name='create_borrower'),
    path("borrowers_list/update/<int:pk>/", UpdateBorrower.as_view(), name='update_borrower'),
    path("borrower/<int:pk>/",
         DetailView.as_view(model=Borrower, template_name="borrower/borrower_detail.html"),
         name="detail_borrower"),
    path("borrowers_list/delete/<int:pk>", DeleteBorrower.as_view(), name='deletion_borrower'),
    path("create_borrowing/<str:name>", create_borrowing, name='create_borrowing'),
    path("delete_borrowing/<str:name>", delete_borrowing, name='delete_borrowing')
]
