from pathlib import Path

data_path = Path('cycle_nested1.py')

with open(data_path, encoding='utf-8') as filein:
    data = filein.readlines()


fruits = dict.fromkeys(data[1:7])
print(fruits)
