fruits = [
    'яблоко', 
    'груша', 
    'персик', 
    'апельсин', 
    'грейпфрут', 
    'слива'
]

for i in range(len(fruits)):
    # замена элемента списка с индексом i
    fruits[i] = fruits[i].upper()

print(fruits)
