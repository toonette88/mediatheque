from django.contrib import admin

from .models import Media, Book, Dvd, Cd, BoardGame

admin.site.register(Media)
admin.site.register(Book)
admin.site.register(Dvd)
admin.site.register(Cd)
admin.site.register(BoardGame)

# Register your models here.
