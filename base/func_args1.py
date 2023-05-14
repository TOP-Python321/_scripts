def add(number1, number2):
    result = number1 + number2
    return result


print(add(7, 13))
print(add(31, 5))
# приведёт к исключению TypeError
# print(add(1))


def sub(number1, number2=0):
    return number1 - number2


print(sub(5, 2))
print(sub(10))
# приведёт к исключению TypeError
# print(sub())


def mul(number1=1, number2=1):
    return number1 * number2


print(mul(5, 9))
print(mul(12))
print(mul())
# приведёт к исключению TypeError
# print(mul(9, 4, 1))


def div(number1=1, number2=1):
    return round(number1 / number2, 1)


print(div(25))
print(div(number2=4), end='\n\n')

# передача аргументов по ключу
print(div(number1=13, number2=2))
print(div(number2=2, number1=13))
# передача аргументов по позиции
print(div(13, 2))
print(div(2, 13))
# передача аргументов по позиции и по ключу
print(div(2, number2=13))
# приведёт к исключению SyntaxError
# print(div(number2=13, 2))
