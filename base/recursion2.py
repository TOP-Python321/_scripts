def gcd(num1: int, num2: int) -> int:
    """Рекурсивная реализиция нахождения наибольшего общего делителя (НОД)"""
    if num1 % num2 == 0:
        print(f'последний шаг рекурсии {num1=} {num2=}')
        return num2
    else:
        print(f'перед рекурсивным вызовом {num1=} {num2=}')
        res = gcd(num2, num1 % num2)
        print(f'возврат рекурсивного вызова {res=}')
        return res


