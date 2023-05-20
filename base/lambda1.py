def func() -> None:
    """"Ничего не делающая функцияю"""


print(func)
print(type(func), end='\n\n')


f1 = lambda: None

print(f1)
print(type(f1), end='\n\n')


f2 = lambda: 'возвращаемое значение'
result = f2()
print(result)


f3 = lambda arg1, arg2, arg3=0: arg1 + arg2 * arg3**arg3
result = f3(2, 4, 5)
print(result)
result = f3(2, 4)
print(result)
result = f3(arg3=2, arg2=10, arg1=7)
print(result)
