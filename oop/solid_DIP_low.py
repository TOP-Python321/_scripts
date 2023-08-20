"""
Dependencies Inversion Principle — Принцип Инверсии Зависимостей

Нижний уровень
"""

from collections.abc import Generator
from dataclasses import dataclass
from enum import Enum


@dataclass
class Person:
    name: str
    
    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.name == other.name
        else:
            raise TypeError
    
    def __repr__(self):
        return f'<{self.name}>'


class Relation(Enum):
    PARENT = 0
    CHILD = 1


class Relationship:
    def __init__(self):
        self.storage: set[tuple[Person, Relation, Person]] = set()
    
    def add_relation(
            self, 
            person1: Person, 
            relation: Relation, 
            person2: Person
    ) -> None:
        self.storage.add((person1, relation, person2))
    
    # нарушение DIP — отсутствуют интерфейсы для взаимодействия с хранилищем
    
    # решение — предоставить интерфейсы
    def find_all_children(self, person: Person) -> Generator[Person]:
        for person1, relation, person2 in self.storage:
            if person1 == person and relation is Relation.PARENT:
                yield person2


db = Relationship()

ivan = Person('Иван')
anna = Person('Анна')
liza = Person('Елизавета')
petr = Person('Пётр')
igor = Person('Игорь')
alla = Person('Алла')

db.add_relation(ivan, Relation.PARENT, liza)
db.add_relation(ivan, Relation.PARENT, petr)
db.add_relation(anna, Relation.PARENT, liza)
db.add_relation(anna, Relation.PARENT, petr)
db.add_relation(igor, Relation.PARENT, alla)

