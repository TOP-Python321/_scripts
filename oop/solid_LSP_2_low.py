"""
Liskov Substitution Principle — Принцип Подстановки Лисков

Нижний уровень
"""

class Rectangle:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        self.area = width * height
    
    @property
    def width(self) -> int:
        return self._width
    
    @width.setter
    def width(self, new_width: int):
        self._width = new_width
        self.area = new_width * self._height
    
    @property
    def height(self) -> int:
        return self._height
    
    @height.setter
    def height(self, new_height: int):
        self._height = new_height
        self.area = self._width * new_height


class Square(Rectangle):
    def __init__(self, side: int):
        super().__init__(side, side)
    
    @Rectangle.width.setter
    def width(self, new_width: int):
        self._width = new_width
        # нарушение LSP — в родительском классе атрибут _height не был зависим от атрибута _width
        self._height = new_width
        self.area = new_width**2
    
    @Rectangle.height.setter
    def height(self, new_height: int):
        # нарушение LSP — в родительском классе атрибут _width не был зависим от атрибута _height
        self._width = new_height
        self._height = new_height
        self.area = new_height**2

