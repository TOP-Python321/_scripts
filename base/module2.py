"""Дополнительный модуль"""

print('\tначало выполнения module2')


from module3 import a as mod2_a, b as mod2_b
print('\tимпорт module3 выполнен')

mod2_b[1] = mod2_a


print('\tконец выполнения module2')