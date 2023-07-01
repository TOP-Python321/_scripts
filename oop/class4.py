class Human:
    head = 1
    hands = 2
    fingers = 5
    legs = 2
    toes = 5
    
    def speak(self, message: str):
        print(self)
        print(message)


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
# igor.speak('привет') -> Human.speak(igor, 'привет')
