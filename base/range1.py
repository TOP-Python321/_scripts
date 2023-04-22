range_obj = range(5)
print(f'{range_obj} {type(range_obj)}\n')

while True:
    right_edge = input(' введите число - правую границу диапазона: ')
    if not right_edge:
        break
    range_obj = range(int(right_edge))
    print(list(range_obj))
print()

while True:
    left_edge = input(' введите число - левую границу последовательности: ')
    if not left_edge:
        break
    right_edge = input(' введите число - правую границу последовательности: ')
    # позиционное присваивание двух объектов справа в две переменных слева (распаковка)
    left_edge, right_edge = int(left_edge), int(right_edge)
    
    range_obj = range(left_edge, right_edge)
    print(list(range_obj))
print()

while True:
    left_edge = input(' введите число - левую границу последовательности: ')
    if not left_edge:
        break
    right_edge = input(' введите число - правую границу последовательности: ')
    step = input(' введите число - шаг последовательности: ')
    # позиционное присваивание трёх объектов справа в три переменных слева (распаковка)
    left_edge, right_edge, step = int(left_edge), int(right_edge), int(step)
    
    range_obj = range(left_edge, right_edge, step)
    print(list(range_obj))
print()

