def calculator(num1: float, num2: float, operation: 'function') -> float:
    """Выполняет произвольную операцию над двумя вещественными числами.
    
    :param num1: вещественное число
    :param num2: вещественное число
    :param operation: вызываемый объект, ожидает два обязательных аргумента
    :returns: вещественное число"""
    return operation(num1, num2)


calculator(5, 9, lambda n1, n2: n1**n2)


operations = [
    lambda n1, n2: n1 + n2,
    lambda n1, n2: n1 - n2,
    lambda n1, n2: n1 * n2,
    lambda n1, n2: n1 // n2,
]
numbers = range(19, 0, -1)

for n1, n2 in enumerate(numbers, 1):
    i = (n1 - 1) % 4
    func = operations[i]
    result = calculator(n1, n2, func)
    print(n1, n2, i, result, sep='\t')

