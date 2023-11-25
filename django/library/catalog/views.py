from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from datetime import datetime as dt

from catalog import models


def hello(request) -> HttpResponse:
    return render(
        request,
        'hello.html',
        {
            'datetime': f'{dt.now():%H:%M %d.%m.%Y}',
        }
    )


def catalog(request) -> HttpResponse:
    template = get_template('catalog/index.html')
    context = {
        'books': models.Book.objects.all(),
        'padding': 20,
    }
    return HttpResponse(template.render(context))

