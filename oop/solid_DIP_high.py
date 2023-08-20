"""
Dependencies Inversion Principle — Принцип Инверсии Зависимостей

Верхний уровень
"""

import solid_DIP_low as storage


class Research:
    def __init__(self, db: storage.Relationship):
        self.db = db
    
    # нарушение DIP — код верхнего уровня использует внутреннюю структуру хранилища
    # def find_all_children(self, person: storage.Person) -> Generator[storage.Person]:
        # for person1, relation, person2 in self.db.storage:
            # if person1 == person and relation is storage.Relation.PARENT:
                # yield person2
    
    # решение — не обращаться к внутренней структуре кода нижнего уровня


r = Research(storage.db)
# children = r.find_all_children(storage.Person('Иван'))
# решение — использовать предоставленные интерфйесы
children = r.db.find_all_children(storage.Person('Иван'))

print(*children, sep='\n')
