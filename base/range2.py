text = input(' введите строку: ')

pos_indexes = range(len(text))
neg_indexes = range(-len(text), 0)

for i in neg_indexes:
    # дополнение слева формируемой строки пробелами, чтобы длина строки была равна указанному числу (3)
    print(f'{i:>3}', end=' ')
print()

for char in text:
    # машиночитаемое представление строки (с кавычками)
    print(f'{char!r}', end=' ')
print()

for i in pos_indexes:
    # дополнение слева и справа формируемой строки пробелами, чтобы длина строки была равна указанному числу (3)
    print(f'{i:^3}', end=' ')
print()
