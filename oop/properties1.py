class Rectangle:
    def __init__(self, a: float, b: float):
        self._a = a
        self._b = b
        self.area = a * b
    
    # def area(self) -> float:
        # return self.a * self.b
    
    @property
    def a(self) -> float:
        print('вызов геттера a')
        return self._a
    
    @a.setter
    def a(self, value: float):
        print('вызов сеттера a')
        self._a = value
        self.area = value * self._b
    
    @property
    def b(self) -> float:
        print('вызов геттера b')
        return self._b
    
    @b.setter
    def b(self, value: float):
        print('вызов сеттера b')
        self._b = value
        self.area = self._a * value
    


r1 = Rectangle(5, 10)

# >>> r1.area
# 50
# >>> 
# >>> r1.a
# вызов геттера
# 5
# >>> r1.a = 3
# вызов сеттера
# >>>
# >>> r1.area
# 30


class Square:
    def __init__(self, side: float):
        self._side = side
        self._perimeter = side*4
        self._area = side**2
    
    @property
    def side(self) -> float:
        return self._side
    
    @side.setter
    def side(self, new_side: float):
        self._side = new_side
        self._perimeter = new_side * 4
        self._area = new_side**2
    
    @property
    def perimeter(self) -> float:
        return self._perimeter
    
    @perimeter.setter
    def perimeter(self, new_perimeter: float):
        self._side = new_perimeter / 4
        self._perimeter = new_perimeter
        self._area = self._side**2
    
    @property
    def area(self) -> float:
        return self._area
    
    @area.setter
    def area(self, new_area: float):
        self._side = new_area**0.5
        self._perimeter = self._side * 4
        self._area = new_area


sq1 = Square(5)

