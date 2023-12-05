from django import forms
from django.core.exceptions import ValidationError

from catalog import models


def check_book_title(value: str):
    if models.Book.objects.filter(
            title__exact=value
    ):
        raise ValidationError(
            f'книга с названием {value!r} уже есть в базе',
            code='matched'
        )


class AddBook(forms.Form):
    title = forms.CharField(
        label='Название книги',
        max_length=100,
        validators=[check_book_title],
        error_messages={
            'matched': 'книга с таким названием уже есть в базе',
        },
    )
    author = forms.CharField(
        label='Автор',
        max_length=100,
        help_text='Имя Фамилия',
    )
    publisher = forms.CharField(
        label='Издательство',
        max_length=100,
    )

