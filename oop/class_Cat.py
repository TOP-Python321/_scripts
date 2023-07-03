from random import choice, randrange as rr
from typing import Self


class Cat:
    """
    Описывает базовое поведение кошки.
    """
    names = ('Мурка', 'Черныш', 'Беляш', 'Рыжик', 'Черепаха', 'Пятно', 'Кошка')
    colors = ('чёрный', 'белый', 'рыжий', 'черепаховый', 'серый', 'пятнистый')
    
    def __init__(
            self, 
            name: str = None, 
            color: str = None, 
            weight: float = 0.2
    ):
        if not name:
            name = choice(self.names)
        self.name = name
        if not color:
            color = choice(self.colors)
        self.color = color
        self.weight = weight
    
    def __repr__(self):
        return f'<Cat: name={self.name}, weight={self.weight}, color={self.color}>'
    
    def __str__(self):
        return self.name
    
    @staticmethod
    def murr():
        print('м' + 'р'*rr(2, 10))
    
    @staticmethod
    def meow(*, long: bool = False) -> None:
        print(' '.join(['мяу']*rr(1, (2, 6)[long])))
    
    def hungry(self) -> None:
        self.meow(long=True)
    
    def eat(self) -> None:
        self.weight += 0.1*rr(1,3)
    
    def hunt(self):
        self.weight -= 0.1
        if choice(range(2)):
            print('успешная охота')
            self.eat()
        else:
            print('неудачная охота')
    
    @classmethod
    def reproduce(cls) -> tuple[Self, Self, ...]:
        return tuple(cls() for _ in range(rr(2, 6)))


yara = Cat('Яра', 'пятнистая', 4.5)

# при вызове объекта класса осуществляется вызов встроенного метода __call__()
# Cat(*args, **kwargs) -> Cat.__call__(Cat, *args, **kwargs)

# примерное представление встроенного метода __call__()
# def __call__(cls, *args, **kwargs):
    # instance = super().__call__(cls)
    # instance.__init__(*args, **kwargs)
    # return instance


kittens = yara.reproduce()

# >>> Cat.reproduce
# <bound method Cat.reproduce of <class '__main__.Cat'>>

# >>> yara.reproduce
# <bound method Cat.reproduce of <class '__main__.Cat'>>

# при вызове классового метода осуществляется вызов от объекта класса с передачей этого же объекта класса в качестве первого позиционного аргумента
# yara.reproduce() -> Cat.reproduce(Cat)
# yara.reproduce() -> yara.__class__.reproduce(yara.__class__)

