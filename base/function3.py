def function_returns_None():
    pass


rv_None = function_returns_None()
print(f'{rv_None}\n{type(rv_None)}')


def function_returns_int():
    return 2 + 3


rv_int = function_returns_int()
print(f'{rv_int}\n{type(rv_int)}')


# 1. вызов function_returns_int()
# 2. возвращаемое значение передаётся в качестве аргумента в range()
# 3. вызов range()
# 4. возвращаемое значение передаётся в качестве аргумента в tuple()
# 5. вызов tuple()
# 6. возвращаемое значение сохраняется в переменную numbers
numbers = tuple(range(function_returns_int()))
print(numbers)
