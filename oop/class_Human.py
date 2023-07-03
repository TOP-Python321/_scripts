class Human:
    head = 1
    hands = 2
    fingers = 5
    legs = 2
    toes = 5
    
    def check_id(self):
        print(id(self))
    
    def rename(self, new_name: str) -> None:
        self.name = new_name
    
    @staticmethod
    def speak(message: str) -> None:
        print(message)
    
    def __repr__(self):
        return f'<Human: name={self.name}>'
    
    def __str__(self):
        return f'Привет, меня зовут {self.name}!'


# атрибуты объекта класса не считая встроенных (начинаются и заканчиваются на '__')
print('\nвнутреннее пространство имён объекта класса')
print({k: v for k, v in Human.__dict__.items() if not k.startswith('__')})

igor = Human()
ilya = Human()
inna = Human()

igor.name = 'Игорь'
ilya.name = 'Илья'
inna.name = 'Инна'

print('\nвнутренние пространства имён экземпляров')
for person in (igor, ilya, inna):
    print(person.__dict__)

print('\nобласти видимости экземпляров')
for person in (igor, ilya, inna):
    print([attr for attr in person.__dir__() if not attr.startswith('__')])


# >>> Human.speak
# <function Human.speak at 0x0000018FF134F880>

# >>> igor.speak
# <bound method Human.speak of <__main__.Human object at 0x0000018FF12F8090>>

# при вызове метода происходит вызов функции от объекта класса с передачей экземпляра в качестве первого позиционного аргумента
# igor.check_id() -> Human.check_id(igor)
# igor.rename('ИГОР') -> Human.rename(igor, 'ИГОР')


# >>> id(ilya)
# 2469153017680

# >>> ilya.check_id()
# 2469153017680


# >>> Human.speak
# <function Human.speak at 0x000001B6EEB9FA60>

# >>> inna.speak
# <function Human.speak at 0x000001B6EEB9FA60>

# >>> inna.speak('привет')
# привет

# >>> Human.speak('привет')
# привет


# >>> igor
# <Human: name=Игорь>

# >>> f'{igor!r}'
# '<Human: name=Игорь>'

# >>> repr(igor)
# '<Human: name=Игорь>'

# >>> igor.__repr__()
# '<Human: name=Игорь>'


# >>> print(igor)
# Привет, меня зовут Игорь!

# >>> f'{igor!s}'
# 'Привет, меня зовут Игорь!'

# >>> str(igor)
# 'Привет, меня зовут Игорь!

# >>> igor.__str__()
# 'Привет, меня зовут Игорь!'
