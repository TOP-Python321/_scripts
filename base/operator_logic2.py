inp = input(' введите число: ')

if inp.isdecimal() or inp[0] == '-' and inp[1:].isdecimal():

# 1 шаг — выражение с оператором or (наименьший приоритет)
#   inp.isdecimal() or inp[0] == '-' and inp[1:].isdecimal()

# 1.1 шаг — левый операнд оператора or
#   inp.isdecimal()

# 1.2 шаг — правый операнд оператора or — выражение с оператором and
#   inp[0] == '-' and inp[1:].isdecimal()

# 1.2.1 шаг — левый операнд оператора and
#   inp[0] == '-'

# 1.2.2 шаг — правый операнд оператора and
#   inp[1:].isdecimal()

    inp = int(inp)
    print(inp ** 2)

else:
    print('вводите число с помощью символов десятичных цифр')
