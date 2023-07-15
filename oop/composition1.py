from typing import Literal


class Person:
    
    # композиция
    class Gender:
        def __init__(self, value: Literal['M', 'F']):
            self.value = value
    
    def __init__(self, name: str, sex: Gender):
        self.name = name
        self.sex = sex

    def __str__(self):
        return self.name

igor = Person('Игорь', Person.Gender('M'))

