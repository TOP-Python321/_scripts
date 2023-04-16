text = 'привет'

print(text)
print(type(text), end='\n\n')

char1 = text[0]
char1_code = ord(char1)

print(f'{char1!r} ({char1_code})')
print(f'{type(char1)} ({type(char1_code)})\n')

next_char = chr(char1_code + 1)
print(f'{next_char!r} ({ord(next_char)})')
