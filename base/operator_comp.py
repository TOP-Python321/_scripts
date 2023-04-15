inp = input(' введите строку: ')

print(f"\n{inp == 'привет' = }")
print(f"{inp != 'привет' = }\n")

print(f"{len(inp) > 6 = }")
print(f"{len(inp) >= 6 = }\n")
print(f"{len(inp) < 10 = }")
print(f"{len(inp) <= 10 = }\n")

print(f"{6 < len(inp) <= 10 = }\n")

bool_obj = inp != 'длинная строка'
print(f'{bool_obj = }\n{type(bool_obj) = }')

# проверка на приндалежность к определённому типу данных
print(f"\n\n{type(inp) is str = }")
