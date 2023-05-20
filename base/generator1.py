def generator_function() -> 'generator':
    yield 1
    yield 1
    yield 2
    yield 3
    yield 5
    yield 8
    yield 13


gen_obj = generator_function()
print(gen_obj)
print(type(gen_obj))

print(gen_obj.__next__())
print(gen_obj.__next__())
print(gen_obj.__next__())
print(gen_obj.__next__())
print(gen_obj.__next__())
print(gen_obj.__next__())
print(gen_obj.__next__())
# приведёт к исключению StopIteration
# print(gen_obj.__next__())



def generator_function2(start: int) -> 'generator':
    """Генератор: вычисляет расходящийся ряд целых чисел от переданного начального числа."""
    for i in range(1, 11):
        yield start + i
        ...
        yield start - i
        ...


diverging_series = generator_function2(0)
# для каждой итерации по объекту вызывается метод объекта __next__()
for n in diverging_series:
    print(n, end=' ')
print()

# повторная попытка проитерироваться по уже полностью вычисленному объекту генетратора каждый раз будет приводить к StopIteration и прерыванию итерации
print(list(diverging_series))
