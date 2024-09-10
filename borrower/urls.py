from django.urls import path, include
from django.contrib.auth.decorators import login_required

from . import views
from .views import BorrowerAutocomplete
from librarian import views as librarian_views


urlpatterns = [
    path('', views.borrower_index, name='borrower_index'),
    path('borrowers_list', views.borrowers_list, name='borrowers_list'),
    path('borrower/update_borrower/<int:id>', librarian_views.modification_borrower, name='update_borrower'),
    path('borrower/autocomplete/',
         BorrowerAutocomplete.as_view(), name='borrower_autocomplete',
         ),

]
