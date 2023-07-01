# регистр для имён переменных и функций: lower_snake_case
# регистр для имён классов: CamelCase

# создание объекта класса
class TestClass:
    pass


# обращение к объекту класса
print(TestClass, end='\n\n')


# создание экземпляра класса
test_instance = TestClass()

# обращение к объекту экземпляра класса
print(test_instance)
print(type(test_instance), end='\n\n')

# в атрибуте __class__ любого экземпляра записана ссылка на объект класса, от которого был создан данный экземпляр
print(f'{id(test_instance.__class__) = }\n'
      # функция type() возвращает значение атрибута __class__ (в некоторых сценариях удобнее использовать функцию, а не обращение к атрибуту)
      f'{id(type(test_instance)) = }\n'
      f'{id(TestClass) = }\n')

print(f'{TestClass is test_instance.__class__ is type(test_instance) = }\n')

print(f'{id(test_instance) = }')
