inp = input(' введите строку: ')

print('\nначало первой серии проверок')

if inp == 'Шаповаленко':
    print(f'Привет, {inp}!')

elif len(inp) > 10:
    print('слишком длинно, как можно сократить?')

print('конец первой серии проверок\n')


print('\nначало второй серии проверок')

if inp == 'Шаповаленко':
    print(f'Привет, {inp}!')

if len(inp) > 10:
    print('слишком длинно, как можно сократить?')

print('конец второй серии проверок\n')
