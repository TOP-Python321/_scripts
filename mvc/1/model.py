"""
Model (MVC): получение данных.
"""

from dataclasses import dataclass
from json import load as jload
from pathlib import Path
from sys import path


people_path = Path(path[0]) / 'people.json'


@dataclass
class Person:
    name: str
    age: int
    email: str
    phone: str
    country: str
    langs: set[str]

    def __repr__(self):
        return f"{self.name} from {self.country} speaks {', '.join(self.langs)}"


def read_all_people() -> list[Person]:
    with open(people_path, encoding='utf-8') as filein:
        raw = jload(filein)
    result = []
    for person in raw:
        person['langs'] = set(person['langs'].split())
        result.append(Person(**person))
    return result


storage: list[Person]


# тесты
if __name__ == '__main__':
    people = read_all_people()
    print(*people, sep='\n')

