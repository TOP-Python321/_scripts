"""Точка входа."""

print('начало выполнения module1')


import module2
print('импорт module2 выполнен')

module1_namespace = {k: v for k, v in globals().items() if not k.startswith('__')}
module2_namespace = {k: v for k, v in module2.__dict__.items() if not k.startswith('__')}

print(module1_namespace, module2_namespace, sep='\n\n', end='\n\n')


from sys import modules

print(module2.mod2_b)
print(modules['module3'].b)

module2.mod2_b[0] = None
print(module2.mod2_b)
print(modules['module3'].b)


print('конец выполнения module1')