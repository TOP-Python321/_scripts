from itertools import chain


class Refrigerator:
    def __init__(self):
        self.refrigerator: list[str] = []
        self.freezer: list[str] = []
        self.temperature: float = 20.0
    
    def __iter__(self):
        return chain(self.refrigerator, self.freezer)
    
    def __len__(self):
        return self.refrigerator.__len__() + self.freezer.__len__()


rf1 = Refrigerator()

# >>> rf1.refrigerator += ['суп', 'молоко', 'сметана']
# >>> rf1.freezer += ['мясо', 'рыба']

# >>> for product in rf1:
# ...     print(product)
# ... 
# суп
# молоко
# сметана
# мясо
# рыба

# >>> len(rf1)
# 5
