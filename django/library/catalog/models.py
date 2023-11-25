from django.db import models


class Author(models.Model):
    
    class Meta:
        db_table = 'authors'
    
    author_id = models.SmallAutoField(
        db_column='author_id',
        primary_key=True
    )
    last_name = models.CharField(
        db_column='last_name',
        max_length=50
    )
    first_name = models.CharField(
        db_column='first_name',
        max_length=50
    )
    
    def __repr__(self):
        return f'{self.last_name} {self.first_name}'


class Book(models.Model):
    
    class Meta:
        db_table = 'books'
    
    book_id = models.AutoField(
        db_column='book_id',
        primary_key=True
    )
    title = models.CharField(
        db_column='title',
        max_length=100
    )
    author = models.ForeignKey(
        to='Author',
        db_column='author_id',
        on_delete=models.CASCADE
    )
    
    def __repr__(self):
        return self.title
    
    def __str__(self):
        return f'{self.author.last_name}. {self.title}'


class Publisher(models.Model):
    
    class Meta:
        db_table = 'publishers'
    
    publisher_id = models.SmallAutoField(
        db_column='publisher_id',
        primary_key=True
    )
    name = models.CharField(
        db_column='name',
        max_length=100
    )
    authors = models.ManyToManyField(
        to='Author'
    )
    books = models.ManyToManyField(
        to='Book'
    )
    
    def __repr__(self):
        return self.name


# > python manage.py shell
# >>> from catalog.models import Book, Author, Publisher
# >>>
# >>> rey = Author(first_name='Рей', last_name='Брэдбери')
# >>> lev = Author(first_name='Лев', last_name='Толстой')
# >>> fed = Author(first_name='Фёдор', last_name='Достоевский')
# >>>
# >>> rey.save()
# >>> lev.save()
# >>> fed.save()
# >>>
# >>> books = (
# ...    Book(title='451° по Фаренгейту', author=rey),
# ...    Book(title='Война и Мир', author=lev),
# ...    Book(title='Преступление и наказание', author=fed),
# ...    Book(title='Бесы', author=fed)
# ... )
# >>> for book in books:
# ...     book.save()
# ...
# >>>
# >>> ast = Publisher(name='АСТ')
# >>> azb = Publisher(name='Азбука')
# >>>
# >>> ast.save()
# >>> azb.save()
# >>>
# >>> ast.books.add(books[0])
# >>> azb.books.add(*books[1:])

