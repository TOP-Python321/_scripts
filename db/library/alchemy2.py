from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy.sql.schema import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String


Base = declarative_base()


author_publisher = Table(
    'authors_publishers',
    Base.metadata,
    Column('author_id', Integer, ForeignKey('authors.id')),
    Column('publisher_id', Integer, ForeignKey('publishers.id')),
)
book_publisher = Table(
    'books_publishers',
    Base.metadata,
    Column('book_id', Integer, ForeignKey('books.id')),
    Column('publisher_id', Integer, ForeignKey('publishers.id')),
)


class Author(Base):
    __tablename__ = 'authors'
    
    id = Column('id', Integer, primary_key=True)
    first_name = Column('first_name', String(30))
    last_name = Column('last_name', String(30))
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(Base):
    __tablename__ = 'books'

    id = Column('id', Integer, primary_key=True)
    title = Column('title', String(50))
    author_id = Column('author_id', Integer, ForeignKey('authors.id'))


class Publisher(Base):
    __tablename__ = 'publishers'
    
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(50))
    authors = relationship('Author', author_publisher)
    books = relationship('Book', book_publisher)



if __name__ == '__main__':
    
    engine = create_engine('sqlite:///library.sqlite3')
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(engine)
    session = Session()
    
    authors_list = [
        Author(id=1, first_name='Лоис', last_name='Буджолд'),
        Author(id=2, first_name='Сергей', last_name='Лукьяненко'),
        Author(id=3, first_name='Рэй', last_name='Брэдбери'),
    ]
    for author in authors_list:
        session.add(author)
    session.flush()
    session.commit()
    
    # select * from authors
    query = session.query(Author)
    data = query.all()
    
    for row in data:
        print(f'{type(row)} — {row}')

