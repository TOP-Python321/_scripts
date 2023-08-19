"""Open/Close Principle — Принцип Открытости/Закрытости"""

from abc import ABC, abstractmethod
from collections.abc import Generator, Iterable
from dataclasses import dataclass
from enum import Enum


class Color(Enum):
    BLACK = '#000'
    RED = '#f00'
    GREEN = '#0f0'
    BLUE = '#00f'
    WHITE = '#fff'

class Size(Enum):
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'


@dataclass
class Product:
    name: str
    color: Color
    size: Size
    
    def __str__(self):
        return f'<{self.name}, {self.color.name}, {self.size.value}>'


goods = [
    Product('Гранат', Color.RED, Size.MEDIUM),
    Product('Арбуз', Color.GREEN, Size.LARGE),
    Product('Виноград', Color.GREEN, Size.SMALL),
    Product('Слива', Color.BLUE, Size.SMALL),
    Product('Хурма', Color.RED, Size.SMALL),
]


# класс ProductBase нарушает OCP
# количество методов для фильтрации будет экспоненциально возрастать с увеличением количества критериев
# a b: a b ab
# a b c: a b c ab bc ac abc
# a b c d: a b c d ab bc cd ac ad bd abc abd bcd abcd

@dataclass
class ProductBase:
    products: list[Product]
    
    def filter_by_color(self, color: Color) -> Generator[Product]:
        for product in self.products:
            if product.color is color:
                yield product
    
    def filter_by_size(self, size: Size) -> Generator[Product]:
        for product in self.products:
            if product.size is size:
                yield product
    
    def filter_by_color_and_size(self, color: Color, size: Size) -> Generator[Product]:
        for product in self.products:
            if product.color is color and product.size is size:
                yield product


# >>> pb = ProductBase(goods)
# >>>
# >>> print(*pb.products, sep='\n')
# Product(name='Гранат', color=<Color.RED: '#f00'>, size=<Size.MEDIUM: 'M'>)
# Product(name='Арбуз', color=<Color.GREEN: '#0f0'>, size=<Size.LARGE: 'L'>)
# Product(name='Виноград', color=<Color.GREEN: '#0f0'>, size=<Size.SMALL: 'S'>)
# Product(name='Слива', color=<Color.BLUE: '#00f'>, size=<Size.SMALL: 'S'>)
# Product(name='Хурма', color=<Color.RED: '#f00'>, size=<Size.SMALL: 'S'>)
# >>>
# >>> print(*pb.filter_by_color(Color.RED), sep='\n')
# <Гранат, RED, M>
# <Хурма, RED, S>
# >>>
# >>> print(*pb.filter_by_size(Size.SMALL), sep='\n')
# <Виноград, GREEN, S>
# <Слива, BLUE, S>
# <Хурма, RED, S>
# >>>
# >>> print(*pb.filter_by_color_and_size(Color.GREEN, Size.LARGE), sep='\n')
# <Арбуз, GREEN, L>


# решение — реализовать цепочку классов для критериев и комбинаций с использованием абстракции и наследования

class Criteria(ABC):
    @abstractmethod
    def match(self, product: Product) -> bool:
        """Проверяет на соответствие определённый параметр переданного продукта."""


@dataclass
class ColorCriteria(Criteria):
    color: Color
    
    def match(self, product: Product) -> bool:
        return product.color is self.color


@dataclass
class SizeCriteria(Criteria):
    size: Size
    
    def match(self, product: Product) -> bool:
        return product.size is self.size


class AndCriteria(Criteria):
    def __init__(self, *criterias: Criteria):
        self.criterias = criterias
    
    def match(self, product: Product) -> bool:
        return all(map(
            lambda c: c.match(product), 
            self.criterias
        ))


@dataclass
class ProductBase:
    products: list[Product]
    
    def filter(self, criteria: Criteria) -> Generator[Product]:
        for product in self.products:
            if criteria.match(product):
                yield product


# >>> pb = ProductBase(goods)
# >>>
# >>> green = ColorCriteria(Color.GREEN)
# >>> red = ColorCriteria(Color.RED)
# >>> med = SizeCriteria(Size.MEDIUM)
# >>> red_and_medium = AndCriteria(red, med)
# >>>
# >>> print(*pb.filter(green), sep='\n')
# <Арбуз, GREEN, L>
# <Виноград, GREEN, S>
# >>>
# >>> print(*pb.filter(med), sep='\n')
# <Гранат, RED, M>
# >>>
# >>> print(*pb.filter(red_and_medium), sep='\n')
# <Гранат, RED, M>

