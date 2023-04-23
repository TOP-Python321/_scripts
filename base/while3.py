while True:
    inp = input(' введите число: ')
    if inp.isdecimal():
        number = int(inp)
        break
    else:
        print('\t число должно быть введено с помощью символов арабских цифр ')
        continue

print(number * (number - 1))
