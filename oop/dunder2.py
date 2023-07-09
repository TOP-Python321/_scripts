from decimal import Decimal as dec


class Fixed:
    separator: str = '.'
    
    def __init__(self, integer: int, fractional: int):
        self.int = integer
        self.frac = fractional
    
    def __repr__(self):
        return f'<Fixed: {self!s}>'
    
    def __str__(self):
        return f'{self.int}{self.separator}{self.frac}'
    
    # вызывается при obj1 + obj2, если у obj1 есть __add__() => obj1.__add__(obj2)
    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.int+other.int, self.frac+other.frac)
        elif isinstance(other, int):
            return self.__class__(self.int+other, self.frac)
        elif isinstance(other, (float, dec)):
            other = self.__class__(*map(int, str(other).split('.')))
            return self + other
    
    # вызывается при obj1 + obj2, если у obj1 нет __add__(), а у obj2 есть __radd__() => obj2.__radd__(obj1)
    def __radd__(self, other):
        if isinstance(other, (int, float, dec)):
            return self + other
    
    def __int__(self):
        return self.int


n1 = Fixed(2, 5)
n2 = Fixed(4, 3)


# >>> n1
# <Fixed: 2.5>
# >>> n2
# <Fixed: 4.3>
# >>>
# >>> print(n1 + n2)
# 6.8
# >>>
