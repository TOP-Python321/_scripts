from random import randrange as rr

left = ord('a')
right = ord('z')

keys = [
    # шаг 4
    ''.join(
        # шаг 4.4
        chr(rr(left, right+1)) 
        # шаги 4.1, 4.2
        for _ in range(5) 
        # шаг 4.3 пропущен
    )
    # шаги 1, 2
    for _ in range(10)
    # шаг 3 пропущен
]


keys = []
for _ in range(10):
    
    word = ''
    for _ in range(5):
        word += chr(rr(left, right+1))
    
    keys += [word]



print(f'\n{type(keys) = }\n{len(keys) = }\n')
print(*keys, sep='\n')
