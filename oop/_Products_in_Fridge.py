from datetime import date, datetime as dt
from itertools import chain


class Product:
    _date_format: str = '%d.%m.%Y'

    def __init__(
            self, 
            name: str, 
            temperature: float, 
            *,
            expired: date | str,
            produced: date | str = date.today()
    ):
        self.name = name
        self.temperature = temperature
        if isinstance(produced, str):
            produced = dt.strptime(produced, self._date_format).date()
        self.produced = produced
        if isinstance(expired, str):
            expired = dt.strptime(expired, self._date_format).date()
        self.expired = expired
    
    def __repr__(self):
        return (f'<Product: {self.name}'
                f', {self.produced:{self._date_format}}'
                f'–{self.expired:{self._date_format}}>')
    
    def __str__(self):
        return self.name
    
    def __bool__(self):
        return date.today() <= self.expired
    
    def __eq__(self, other):
        return (
                self.name == other.name 
            and self.produced == other.produced 
            and self.expired == other.expired
        )



class Fridge:
    def __init__(self):
        self.refrigerator: list[Product] = []
        self.freezer: list[Product] = []
        self.temperature: float = 20.0
    
    def __iter__(self):
        return chain(self.refrigerator, self.freezer)
    
    def __len__(self):
        return self.refrigerator.__len__() + self.freezer.__len__()
    
    def __contains__(self, item: Product | str):
        if isinstance(item, Product):
            return item in self.__iter__()
        elif isinstance(item, str):
            return item in (prod.name for prod in self)
    
    def get_expired(self) -> list[Product]:
        return [prod for prod in self.refrigerator if not prod]
    
    def clear_expired(self):
        for exp_prod in self.get_expired():
            self.refrigerator.remove(exp_prod)



# >>> milk1 = Product('молоко', 4.5, expired='16.07.2023')
# >>> milk2 = Product('молоко', 4.5, produced='27.06.2023', expired='04.07.2023')
# >>> 
# >>> bool(milk1)
# True
# >>> bool(milk2)
# False


kitchen_fridge = Fridge()

kitchen_fridge.refrigerator += [
    Product('молоко', 4.5, expired='16.07.2023'),
    Product('сметана', 5.0, produced='25.06.2023', expired='08.07.2023')
]

