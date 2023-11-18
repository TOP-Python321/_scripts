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

