from django.contrib import admin
from .models import Book, BookNumber


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'description']
    list_filter = ['published']
    search_fields = ['title', 'description']


admin.site.register(BookNumber)
