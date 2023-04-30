cyrillic = {chr(code) for code in range(1072, 1104)} | {'ё'}
print(len(cyrillic))


for char in cyrillic:
    print(char, end=' ')
print('\n')


print('я' in cyrillic)
print(' ' not in cyrillic)
