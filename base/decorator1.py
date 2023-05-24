def decorator(function: 'callable') -> 'callable':
    print('начало выполнения функции decorator')
    
    def wrapper(*args, **kwargs) -> 'any':
        print('\tначало выполнения функции wrapper')
        result = function(*args, **kwargs)
        print('\tконец выполнения функции wrapper')
        return result
    
    print('конец выполнения функции decorator')
    return wrapper


def test_function():
    print('\t\tвыполнение функции test_function')


print(test_function)
test_function()
print()

test_function = decorator(test_function)
print()

print(test_function)
test_function()
print()


def adder(number1, number2):
    return number1 + number2


print(adder)
result = adder(1, 2)
print(result, end='\n\n')

adder = decorator(adder)
print()

print(adder)
result = adder(3, 4)
print(result, end='\n\n')


@decorator
def product(numbers: list[float]) -> float:
    prod = 1
    for n in numbers:
        prod *= n
    return prod
# product = decorator(product)

result = product(range(3, 16, 3))
print(result)

