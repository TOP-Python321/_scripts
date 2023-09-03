"""Демонстратор Хранителя: сохранение состояний в журнале в атрибуте изменяемого класса."""

from dataclasses import dataclass


@dataclass
class Memento:
    """Хранитель."""
    balance: int


class FixedLengthList(list):
    """Список с ограничением максимального количества элементов."""
    def __init__(self, max_length: int):
        super().__init__()
        self.max_len = max_length

    def append(self, __object) -> None:
        """При достижении максимального количества элементов удаляет первый по счёту элемент и добавляет новый."""
        if len(self) == self.max_len:
            self.pop(0)
        super().append(__object)


class BankAccount:
    """Описывает основные операции с банковским счётом."""
    overdraft_limit = -500
    history_length: int = 100

    def __init__(self, start_balance: int = 0):
        self.__balance = start_balance
        # история изменений фиксированной длины
        self.__history: FixedLengthList[Memento] = FixedLengthList(self.history_length)
        self.__history.append(Memento(start_balance))
        # индекс текущего состояния
        self._index: int = 0

    def deposit(self, amount: int):
        self.__balance += amount
        self.__history.append(Memento(self.__balance))
        if self._index < self.history_length - 1:
            self._index += 1

    def withdraw(self, amount: int):
        result = self.__balance - amount
        if result >= self.overdraft_limit:
            self.__balance = result
            self.__history.append(Memento(result))
            if self._index < self.history_length - 1:
                self._index += 1

    def show_history(self, reverse: bool = False):
        step = (1, -1)[reverse]
        return '\n'.join(repr(state) for state in self.__history[::step])

    def undo(self):
        if self._index > 0:
            self._index -= 1
            self.__balance = self.__history[self._index].balance

    def redo(self):
        if self._index < len(self.__history) - 1:
            self._index += 1
            self.__balance = self.__history[self._index].balance

    def __str__(self):
        return f'баланс: {self.__balance}'


BankAccount.history_length = 5
ba1 = BankAccount(40)

ba1.deposit(50)
ba1.withdraw(310)
ba1.deposit(230)
ba1.deposit(120)
print(ba1.show_history(), end='\n'*2)

ba1.deposit(1000)
print(ba1.show_history(), end='\n'*2)

ba1.undo()
print(ba1)
ba1.undo()
print(ba1)
ba1.undo()
print(ba1)
ba1.undo()
print(ba1)
# без изменений
ba1.undo()
print(ba1, end='\n'*2)

ba1.redo()
print(ba1)
ba1.redo()
print(ba1)
ba1.redo()
print(ba1)
ba1.redo()
print(ba1)
# без изменений
ba1.redo()
print(ba1, end='\n'*2)
