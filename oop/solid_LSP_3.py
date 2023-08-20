"""Liskov Substitution Principle — Принцип Подстановки Лисков"""

from collections.abc import Iterable
from numbers import Number
from typing import Any


class DictOfRange(dict):
    """
    Словарь диапазонов: при использовании объекта Number в качестве ключа возвращает значение, соответствующее кортежу, в диапазон которого попадает объекта Number.
    """
    def __init__(self, kwargs: dict[Iterable[Number, Number], Any]):
        try:
            for left, right in kwargs:
                if not isinstance(left, Number) or not isinstance(right, Number):
                    raise ValueError(f'keys for {self.__class__.__name__!r} must be (Number, Number) objects')
        except TypeError:
            raise ValueError(f'keys for {self.__class__.__name__!r} must be (Number, Number) objects')
        super().__init__(kwargs)
    
    def __getitem__(self, item: Number):
        if isinstance(item, Number):
            for left, right in self:
                if left <= item < right:
                    return super().__getitem__((left, right))
        else:
            # нарушение LSP — невозможно обращение по ключу словаря Iterable[Number, Number]
            # raise TypeError
            
            # решение — если объект, используемый в качестве ключа, не является числом, то попытаться получить значение по ключу
            return super().__getitem__(item)


health = DictOfRange({
    (0, 10): 'при смерти',
    (10, 35): 'тяжело ранен',
    (35, 80): 'ранен',
    (80, 100): 'здоров',
})

# нарушение LSP
# >>> health[(0, 10)]
# ...
# TypeError

