"""Демонстратор Хранителя: сохранение состояний в отдельных объектах."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Memento:
    """Хранитель."""
    balance: int


class BankAccount:
    """Описывает основные операции с банковским счётом."""
    overdraft_limit = -500

    def __init__(self, start_balance: int = 0):
        self.__balance = start_balance

    def deposit(self, amount: int) -> Memento:
        self.__balance += amount
        return Memento(self.__balance)

    def withdraw(self, amount: int) -> Optional[Memento]:
        if self.__balance - amount >= self.overdraft_limit:
            self.__balance -= amount
            return Memento(self.__balance)
        else:
            pass

    def restore(self, memento: Memento):
        self.__balance = memento.balance

    def __str__(self):
        return f'баланс: {self.__balance}'


ba = BankAccount(1000)
print('стартовое значение', ba)

m1 = ba.deposit(500)
m2 = ba.deposit(3000)
m3 = ba.withdraw(2200)

print('после всех операций', ba)

ba.restore(m2)
print('предпоследнее состояние', ba)

ba.restore(m1)
print('ещё более раннее состояние', ba)

