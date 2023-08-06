from abc import ABC, abstractmethod
from random import randrange, sample


class BaseCreature(ABC):
    """
    Абстрактный базовый класс для всех игровых существ.
    """
    def __init__(self, health: int):
        self.health = health

    @abstractmethod
    def die(self):
        """Любое игровое существо может быть уничтожено."""


class Enemy(BaseCreature, list):
    """
    Игровые противники (мобы).
    """
    def __init__(self, health: int):
        super().__init__(health)
        self.__generate_drop()

    def __generate_drop(self):
        """Генерируются предметы, выпадающие из моба при уничтожении."""
        self.append(randrange(2, 10))
        self.append('оружие')

    def die(self):
        """При уничтожении моба выпадает случайное количество предметов."""
        return sample(self, k=randrange(4))

    def __repr__(self):
        return (f"<Enemy: HP={self.health}, "
                f"[{', '.join(str(n) for n in self)}]>")


class Trader(BaseCreature):
    """
    Существа, обсуживающие игровую экономику.
    """
    def die(self):
        """Убийство торговцев наказуемо."""
        print('за вами выехали')



mob1 = Enemy(80)
print(mob1, end='\n\n')
print(mob1.die(), end='\n\n')

trader = Trader(500)
trader.die()
