from abc import ABC
from dataclasses import dataclass
from enum import Enum


@dataclass
class Contact:
    mobile: str | None
    office: str | None
    email: str | None


class Person(ABC):

    class Sex(Enum):
        MALE = 'мужской'
        FEMALE = 'женский'

    def __init__(self, sex: Sex):
        ...
        self.sex = sex
        ...


