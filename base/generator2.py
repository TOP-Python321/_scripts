def infinite_counter(start: int, step: int = 1) -> 'generator':
    """Генератор: условно-бесконечный счётчик с настраиваемым шагом."""
    while True:
        yield start
        start += step


for n in infinite_counter(0):
    print(n, end=' ')
