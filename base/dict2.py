char_codes = {
    'а': 10,
    'б': 11,
    'в': 12,
    'г': 13,
    'д': 14,
    'е': 15,
    'ё': 16,
}
print(char_codes, id(char_codes), sep='\n', end='\n\n')

char_codes['в'] = 10
print(char_codes, id(char_codes), sep='\n', end='\n\n')

char_codes |= {'ж': 17, 'з': 18}
print(char_codes, id(char_codes), sep='\n', end='\n\n')

char_codes2 = char_codes | {'ж': 17, 'з': 18}
print(char_codes2, id(char_codes2), sep='\n', end='\n\n')

char_codes_inverted = {v: k for k, v in char_codes.items()}
# то же самое:
# char_codes_inverted = dict( (v, k) for k, v in char_codes.items() )
print(char_codes_inverted, id(char_codes_inverted), sep='\n', end='\n\n')
