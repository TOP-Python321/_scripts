def person_about(name: str):
    print(f'Имя человека: {name}')

def pet_about(name: str):
    print(f'Кличка питомца: {name}')


about = (person_about, pet_about)
names = [
    input(' имя человека > '),
    input(' кличка питомца > '),
]

for func, name in zip(about, names):
    func(**{'name': name})

