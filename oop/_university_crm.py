from abc import ABC
from enum import Enum


class Person(ABC):

    class Sex(Enum):
        MALE = 'мужской'
        FEMALE = 'женский'

    def __init__(self, sex: Sex):
        ...
        self.sex = sex
        ...


