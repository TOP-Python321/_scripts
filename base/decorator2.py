from functools import wraps


def cache(function):
    arg_res = {}
    @wraps(function)
    def wrapper(num1, num2):
        """обёртка"""
        # получение доступа на запись к локальному пространству имён функции cache()
        nonlocal arg_res
        res = arg_res.get((num1, num2))
        if res is None:
            res = function(num1, num2)
            # пересоздание словаря
            arg_res |= {(num1, num2): res}
        return res
    return wrapper


@cache
def adder(num1, num2):
    """сложение чисел"""
    return num1 + num2

@cache
def subber(num1, num2):
    """вычитание чисел"""
    return num1 - num2

@cache
def mult(num1, num2):
    return num1 * num2

@cache
def div(num1, num2):
    return num1 / num2


print(adder(1, 5))
print(subber(2, 4))

print(adder(1, 5))
print(subber(2, 4))
