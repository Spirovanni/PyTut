from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book


class Another(View):

    book = Book.objects.get(id=2)
    output = f"We have {book.title} book with ID {book.id}<br>"

    # for book in books:
    #     output += f"We have {book.title} books in ID {book.id}<br>"

    def get(self, request):
        return HttpResponse(self.output)


def first(request):
    return HttpResponse('First message from views')
