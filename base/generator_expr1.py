squares = []
for num in range(2, 10):
    squares += [num**2]


squares_gen = (num**2 for num in range(2, 10))


print(f'\n{squares}\n{type(squares)}\n'
      f'\n{squares_gen}\n{type(squares_gen)}\n')

# генератор вычисляет элементы во время итерации
a = list(squares_gen)
    # a = []
    # for num in squares_gen:
        # a += [num]

# это можно сделать только один раз — список b будет пустым
b = list(squares_gen)
    # b = []
    # for num in squares_gen:
        # b += [num]

print(a, b, sep='\n')
