from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path('lists', views.mediaslist),
    path('create_media', views.createmedia),
    path('create_media/book', views.addbook),
    path('create_media/dvd', views.adddvd),
    path('create_media/cd', views.addcd),
]