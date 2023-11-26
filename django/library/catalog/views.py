from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import get_template

from datetime import datetime as dt

from catalog import models


publishers_cache = {
    pub.url: pub
    for pub in models.Publisher.objects.all()
}


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
        'publishers': publishers_cache.values(),
    }
    return HttpResponse(template.render(context))


def publisher(request, publisher: str) -> HttpResponse:
    return render(
        request,
        'catalog/publisher.html',
        {
            'publisher': publishers_cache[publisher],
            'publisher_books': publishers_cache[publisher].books.all(),
        }
    )

