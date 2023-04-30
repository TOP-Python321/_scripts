mammals = {
    'тигр',
    'верблюд',
    'овца',
    'кит',
    'морж',
}
aquatic = {
    'осьминог',
    'креветка',
    'краб',
    'кит',
    'морж',
}
aquatic_mammals = {
    'кит',
    'морж',
}

print(mammals, aquatic, aquatic_mammals, sep='\n', end='\n\n')

print(f'{aquatic_mammals <= mammals = }')
print(f'{aquatic >= aquatic_mammals = }\n')

print(f'{aquatic | mammals = }')
print(f'{aquatic & mammals = }')
# print(aquatic & mammals == aquatic_mammals)
print(f'{aquatic - mammals = }')
print(f'{mammals - aquatic = }')
print(f'{mammals ^ aquatic = }\n')
# print(mammals ^ aquatic == (mammals | aquatic) - (aquatic & mammals))

reptiles = {'черепаха', 'змея', 'ящерица', 'крокодил'}
print(mammals.isdisjoint(reptiles))
# то же самое
print(not bool(mammals & reptiles))

