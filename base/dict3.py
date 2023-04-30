phrases1_weighted = {
    'hello': 0.9,
    'how are you': 0.8,
    "what's up": 0.5,
    'bad day to see you': 0.3,
}

phrases2_weighted = {
    'hello': 0.85,
    'how are you': 0.7,
    "what's up": 0.65,
    'go away': 0.2,
}

# при объединении (слиянии) словарей, значения для совпадающих ключей будут взяты из самого правого словаря
result = phrases1_weighted | phrases2_weighted
print(result)


