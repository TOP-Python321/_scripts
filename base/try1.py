while True:
    try:
        number = int(input(' введите число: '))
    except ValueError:
        print('\t число должно быть введено с помощью символов арабских цифр ')
        continue
    else:
        break

print(number * (number - 1))
