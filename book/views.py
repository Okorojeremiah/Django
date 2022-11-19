from http import HTTPStatus

from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'books/index.html', status=HTTPStatus.ACCEPTED)
