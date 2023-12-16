from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import get_template
from django.views.generic import ListView, DetailView

from datetime import datetime as dt

from catalog import models
from catalog import forms


publishers_cache = {
    pub.url: pub
    for pub in models.Publisher.objects.all()
}


def hello(request) -> HttpResponse:
    print(f'\nDEBUG:\n  {request.user.__class__.__name__}\n  {request.user.get_username()}\n')
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
        'title': 'Каталог',
        'books': models.Book.objects.all(),
        'padding': 20,
        'publishers': publishers_cache.values(),
        'user': request.user,
    }
    return HttpResponse(template.render(context))


def publisher(request, publisher: str) -> HttpResponse:
    return render(
        request,
        'catalog/publisher.html',
        {
            'title': publishers_cache[publisher].name,
            'publisher_books': publishers_cache[publisher].books.all(),
        }
    )


class Publisher(DetailView):
    model = models.Publisher
    template_name = 'catalog/publisher.html'
    
    def get_object(self, queryset=None):
        # print(f'\nDEBUG:\n\t{self.kwargs = }\n')
        return publishers_cache[self.kwargs[self.slug_url_kwarg]]
    
    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        # print(f'\nDEBUG:\n\t{context = }\n')
        return {
            'title': self.object.name,
            'publisher_books': self.object.books.all(),
            # 'is_publisher': self.request.user.groups.filter(name__exact="publishers"),
            'is_publisher': self.request.user.has_perm('catalog.add_book'),
        }


def test(request):
    return render(
        request,
        'catalog/test.html',
    )


def test_sub(request):
    return render(
        request,
        'catalog/test_sub.html',
    )


def add_book(request) -> HttpResponse:
    # вместо django.contrib.auth.decorators.login_required()
    if (
             request.user.is_anonymous
          or not request.user.has_perm('catalog.add_book')
       ):
        return HttpResponseRedirect('/login')
    
    if request.method == 'GET':
        form = forms.AddBook(label_suffix=': ')
    
    elif request.method == 'POST':
        # print(request.POST)
        form = forms.AddBook(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            first_name, last_name = form.cleaned_data['author'].split()
            try:
                author = models.Author.objects.get(
                    last_name__exact=last_name,
                    first_name__exact=first_name
                )
            except ObjectDoesNotExist:
                author = models.Author(
                    last_name=last_name,
                    first_name=first_name
                )
                author.save()
            book = models.Book(
                title=form.cleaned_data['title'], 
                author=author
            )
            book.save()
            # try:
            #     publisher = models.Publisher.objects.get(
            #         name__exact=form.cleaned_data['publisher']
            #     )
            # except ObjectDoesNotExist:
            #     publisher = models.Publisher(
            #         name=form.cleaned_data['publisher']
            #     )
            #     publisher.save()
            # print(request.user.publisher)
            request.user.publisher.books.add(book)
            form = forms.AddBook(label_suffix=': ')
    
    return render(
        request,
        'catalog/add_book.html',
        {
            'title': 'Добавить книгу',
            'form': form
        }
    )


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')
