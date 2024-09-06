from django.urls import path

import authentication.views
from . import views as librarian_views

urlpatterns = [
    path("", librarian_views.index, name='index'),
    path('medias_list', librarian_views.medias_list, name='medias_list'),
    path('create_media', librarian_views.create_media, name='create_media'),
    path('create_media/book', librarian_views.add_book, name='create_media/book'),
    path('create_media/dvd', librarian_views.add_dvd, name='create_media/dvd'),
    path('create_media/cd', librarian_views.add_cd, name='create_media/cd'),
    path('create_borrowing_cd/<int:id>', librarian_views.add_borrowing_cd, name='borrowing_cd'),
    path('create_borrowing_dvd/<int:id>', librarian_views.add_borrowing_dvd, name='borrowing_dvd'),
    path('create_borrowing_book/<int:id>', librarian_views.add_borrowing_book, name='borrowing_book'),
    path('create_borrower', librarian_views.add_borrower, name='create_borrower'),
]
