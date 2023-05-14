def pos_or_neg_or_zero(number):
    if number > 0:
        return 'положительное'
    elif number < 0:
        return 'отрицательное'
    else:
        return 'ноль'
    # эта строка никогда не будет выполнена
    print('конец работы функции')


print(pos_or_neg_or_zero(0))


def odd_or_even(number):
    if number % 2:
        result = 'нечётное'
    else:
        result = 'чётное'
    
    result = result.upper()
    return result


print(odd_or_even(13))
print(odd_or_even(22))
