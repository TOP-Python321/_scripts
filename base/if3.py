num = int(input(' введите число: '))

if num:
    print('не ноль')

    if num % 2:
        print('нечётное')
    else:
        print('чётное')
else:
    print('ноль')
