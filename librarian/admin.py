from django.contrib import admin

from .models import Media, Book, Dvd, Cd, BoardGame, Borrowing

admin.site.register(Book)
admin.site.register(Dvd)
admin.site.register(Cd)
admin.site.register(BoardGame)
admin.site.register(Borrowing)


class Borrowing(admin.ModelAdmin):
    list_display = ('name', 'borrower')
# Register your models here.
