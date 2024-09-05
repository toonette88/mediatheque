from django.urls import path, include

from . import views

urlpatterns = [
    path('borrowers_list', views.borrowers_list, name='borrowers_list'),

]
