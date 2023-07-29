from collections.abc import Iterable
from numbers import Number
from typing import Self


class Vector(list):
    def __init__(self, *numbers: int):
        for n in numbers:
            if not isinstance(n, Number):
                raise ValueError(f'{self.__class__.__name__!r} constructor expects only numbers as arguments')
        else:
            super().__init__(numbers)
            self.n = len(self)

    def append(self, __object: Number) -> None:
        if not isinstance(__object, Number):
            raise ValueError(f'{self.__class__.__name__!r} may contain only numbers')
        super().append(__object)
        self.n += 1

    def extend(self, __iterable: Iterable[Number]) -> None:
        __iterable = tuple(__iterable)
        for n in __iterable:
            if not isinstance(n, Number):
                raise ValueError(f'{self.__class__.__name__!r} may contain only numbers')
        super().extend(__iterable)
        self.n += len(__iterable)

    # self + other
    def __add__(self, other) -> Self:
        if isinstance(other, Number):
            return self.__class__(*(n + other for n in self))
        elif isinstance(other, self.__class__):
            if self.n != other.n:
                raise ValueError('')
            return self.__class__(*(self[i] + other[i] for i in range(self.n)))
        else:
            raise TypeError

    # other + self
    def __radd__(self, other) -> Self:
        return self.__add__(other)

    # self += other
    def __iadd__(self, other) -> Self:
        if isinstance(other, Number):
            for i, n in enumerate(self):
                self[i] = n + other
        elif isinstance(other, self.__class__):
            if len(self) != len(other):
                raise ValueError('')
            for i, n in enumerate(self):
                self[i] = n + other[i]
        else:
            raise TypeError

        return self

    def __neg__(self):
        return self.__class__(*(-n for n in self))

    def __sub__(self, other):
        if isinstance(other, Number):
            return self.__class__(*(n - other for n in self))
        elif isinstance(other, self.__class__):
            if len(self) != len(other):
                raise ValueError('')
            return self.__class__(*(n - other[i] for i, n in enumerate(self)))
        else:
            raise TypeError

    def __isub__(self, other):
        if isinstance(other, Number):
            for i, n in enumerate(self):
                self[i] = n - other
        elif isinstance(other, self.__class__):
            if len(self) != len(other):
                raise ValueError('')
            for i, n in enumerate(self):
                self[i] = n - other[i]
        else:
            raise TypeError
        return self


v1 = Vector(1, 2, 3)
print(v1)

try:
    v2 = Vector('-3', '-1', '1')
except ValueError as exc:
    print(f'{exc.__class__.__name__}: {exc}')
else:
    print(v2)

