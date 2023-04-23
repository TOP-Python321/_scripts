numbers = range(3, 12, 4)

# неявная распаковка
num1, num2, num3 = numbers
print(num1, num2, num3, sep='\n', end='\n\n')

# явная распаковка с использованием оператора *
print(*numbers, sep='\n', end='\n\n')
