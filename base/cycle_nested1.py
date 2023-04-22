fruits = [
    'яблоко', 
    'груша', 
    'персик', 
    'апельсин', 
    'грейпфрут', 
    'слива'
]

for fruit in fruits:
    
    for char in fruit:
        # char_code = ord(char)
        # new_char = chr(char_code + 1)
        # print(new_char, end='')
        print(chr(ord(char) + 1), end='')
    
    print()
