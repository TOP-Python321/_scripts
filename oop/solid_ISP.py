"""Interface Segregation Principle — Принцип Разделения Интерфейсов"""

from abc import ABC, abstractmethod


class MultiFunctionDevice(ABC):
    @abstractmethod
    def print():
        pass
    
    # нарушение ISP — несколько интерфейсов объединены в одном классе
    
    @abstractmethod
    def scan():
        pass
    
    @abstractmethod
    def fax():
        pass


class XeroxML100(MultiFunctionDevice):
    def print():
        print('печать документа')
    
    def scan():
        print('сканирование документа')
    
    def fax():
        print('отправка документа по факсу')


class BrotherHL5250(MultiFunctionDevice):
    def print():
        print('печать документа')
    
    # лишние атрибуты
    def scan():
        raise NotImplementedError
    
    def fax():
        raise NotImplementedError


# решение — предоставить отдельный класс для каждого интерфейса

class Printer(ABC):
    @abstractmethod
    def print():
        pass


class Scanner(ABC):
    @abstractmethod
    def scan():
        pass


class Fax(ABC):
    @abstractmethod
    def fax():
        pass


class XeroxML100(Printer, Scanner, Fax):
    def print():
        print('печать документа')
    
    def scan():
        print('сканирование документа')
    
    def fax():
        print('отправка документа по факсу')


class BrotherHL5250(Printer):
    def print():
        print('печать документа')
    

