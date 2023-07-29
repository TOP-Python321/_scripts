from json import loads
from pathlib import Path
from sys import path


file_path = Path(path[0]) / 'numbers_ru.json'
numbers_ru = loads(file_path.read_text(encoding='utf-8'))
file_path = Path(path[0]) / 'numbers_en.json'
numbers_en = loads(file_path.read_text(encoding='utf-8'))


class IntExtra(int):
    language: str = 'ru'

    def __init__(self, value: int):
        ranks = []
        value, rem = divmod(value, 100)
        if 10 < rem < 20:
            value *= 10
            ranks += [rem]
        else:
            value = value*100 + rem
        while value > 0:
            value, rem = divmod(value, 10)
            ranks += [rem]
        self.ranks = [digit*10**exp for exp, digit in enumerate(ranks)][::-1]

    def __str__(self):
        return ' '.join(
            globals()[f'numbers_{self.language}'][str(rank)]
            for rank in self.ranks
        ).replace('  ', ' ')


# IntExtra(5)
#   IntExtra.__call__(5)
#     self = super().__new__(IntExtra, 5)
#     self.__init__(5)
#     return self

