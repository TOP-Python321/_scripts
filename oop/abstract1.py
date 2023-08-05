from abc import ABC, abstractmethod


class Table(ABC):
    legs = 4
    
    def __init__(self, height: int):
        self.height = height
    
    @abstractmethod
    def __str__(self):
        pass


class ComputerTable(Table):
    def __init__(self, height: int, keyboard_shelf: bool):
        super().__init__(height)
        self.keyboard_shelf = keyboard_shelf
    
    def __str__(self):
        return 'ct'


class DiningTable(Table):
    
    def __str__(self):
        return 'dt for six person'


# table1 = Table(80)
comp_table1 = ComputerTable(65, False)
