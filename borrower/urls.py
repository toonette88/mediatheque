from django.urls import path

from . import views

urlpatterns = [
    path('', views.borrower_index, name='borrower_index'),
    path('borrowers_list', views.borrowers_list, name='borrowers_list'),

]
