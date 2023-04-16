text = 'Python is cool!'

print(text, len(text))

print(text[10])
print(text[-1], end='\n\n')

print(text[7:9])
# repr() — машиночитаемое строковое представление объекта
print(repr(text[0:7]))
print(repr(text[:6]))
print(repr(text[1:-1]))
print(repr(text[-12:5]), end='\n\n')

print(text[10:20])
print(text[10:])
print(text[:], end='\n\n')

print(repr(text[0:6:2]))
print(repr(text[0:7:2]), end='\n\n')

print(text[8:6:-1])
print(text[5::-1])
print(text[::-2], end='\n\n')
