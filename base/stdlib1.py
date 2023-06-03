from decimal import Decimal as dec

numbers = [
    dec(0.1),
    dec('0.1'),
    dec(12),
    dec('34')
]

print(*numbers, sep='\n', end='\n\n')

for num1, num2 in zip(numbers, range(1, 5)):
    res = num2 + num1
    print(res, type(res))
print()


from fractions import Fraction as frac

rationals = [
    frac(1, 4),
    frac('1/3'),
    frac('0.1'),
    frac(0.1),
    frac(dec('0.1')),
]

print(*rationals, sep='\n', end='\n\n')
print(*(
    f'numerator={num.numerator} denominator{num.denominator}' 
    for num in rationals
), sep='\n', end='\n\n')


