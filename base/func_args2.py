def product(number1, number2, *numbers):
    # print(f'{number1} {type(number1)}')
    # print(f'{number2} {type(number2)}')
    # print(f'{numbers} {type(numbers)}')
    numbers = (number1, number2) + numbers
    product = 1
    for num in numbers:
        product *= num
    return product


print(product(3, 5))
print(product(2, 4, 6))
print(product(2, 3, 5, 10))


def round_product(*reals, digits=1):
    product = 1.0
    for num in reals:
        product *= num
    return round(product, digits)


print(round_product())
print(round_product(2.36))
print(round_product(1.1, 2.2, 3.3, digits=3))
