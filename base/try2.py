numbers = tuple(range(-10, 11))

try:
    i = int(input(' введите первый индекс: '))
    j = int(input(' введите второй индекс: '))
    div = numbers[i] // numbers[j]
    rem = numbers[i] % numbers[j]

except ValueError:
    print('\t индекс должен быть введён с помощью символов арабских цифр ')

except IndexError:
    print(f'\t индексы должны находиться в диапазоне от 0 до {len(numbers)-1} включительно ')

except ZeroDivisionError:
    print('\t деление на ноль невозможно ')

else:
    print(div, rem)

