test_dict = {'a': 1, 'b': 2, 0.01: ['float', 'key'], ('Z', '90', 1): 'tuple key'}

print(f'{test_dict}\n{type(test_dict)}\n{len(test_dict) = }\n')

print(test_dict['a'] + test_dict['b'], end='\n\n')

dict_to_list = list(test_dict)
print(dict_to_list)

for key in test_dict:
    print(f'{key = }\t{test_dict[key] = }')
print()

print(test_dict.values())
for value in test_dict.values():
    print(value)
print()

print(test_dict.items())
for item in test_dict.items():
    print(f'{item = }\t{type(item)}')
print()
for key, value in test_dict.items():
    print(f'{key = }\t{value = }')
print()

