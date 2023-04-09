int_var = 368
# print('int_var =', int_var)
# print(f'int_var = {int_var}')
print(f'{int_var = }')
print(f'{type(int_var) = }\n')

# преобразование в int
print(f'{int(2.89) = }')
print(f'{int("52") = }')
print(f'{int(True) = }')
print(f'{int(False) = }\n')
# приведёт к ошибке
# print(f"{int('5.2') = }")
# print(f'{int(3+4j) = }')
# print(f"{int('12bc') = }")


bool_var = True
print(f'{bool_var = }')
print(f'{type(bool_var) = }\n')

print(f'{bool(0) = }')
print(f'{bool(0.0) = }')
print(f'{bool(0+0j) = }')
print(f'{bool("") = }')
print(f'{bool([]) = }')
print(f'{bool({}) = }\n')

print(f'{bool(-12) = }')
print(f'{bool(0.0001) = }')
print(f'{bool(0-1j) = }')
print(f'{bool(" ") = }')
print(f'{bool(["", 0]) = }')
print(f'{bool({"": 0}) = }\n')


float_var = 0.1
print(f'{float_var = }')
print(f'{type(float_var) = }\n')

print(f'{float(17) = }')
print(f'{float("3.1415") = }')
print(f'{float(True) = }')
print(f'{float(False) = }\n')
# приведёт к ошибке
# print(f'{float("3,1415") = }')
# print(f'{float(1+4j) = }')


str_var = "Aa Zz Аа Яя"
print(f'{str_var = }')
print(f'{type(str_var) = }\n')

print(f'{str(37) = }')
print(f'{str(3.141592) = }')
print(f'{str(True) = }')
print(f'{str(False) = }')
print(f'{str([1, 2, 3, 4]) = }')
print(f'{str({"a": 12, "b": 34}) = }')

