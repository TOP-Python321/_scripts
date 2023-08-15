from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import date, datetime as dt
from decimal import Decimal as dec
from enum import Enum
from typing import Literal


@dataclass
class Contact:
    mobile: str = None
    office: str = None
    email: str = None


class Person(ABC):

    class Sex(Enum):
        MALE = 'мужской'
        FEMALE = 'женский'

    _default_date_format: str = '%d.%m.%Y'

    def __init__(
            self,
            last_name: str,
            first_name: str,
            patr_name: str,
            sex: Sex,
            birthdate: date | str | tuple[str, str],
            contacts: Contact,
    ):
        self.last_name = last_name
        self.first_name = first_name
        self.patr_name = patr_name
        self.__fio: str = f'{self.last_name} {self.first_name} {self.patr_name}'
        self.sex = sex
        if isinstance(birthdate, tuple):
            try:
                date_, format_ = birthdate
                assert isinstance(date_, str)
                assert isinstance(format_, str)
            except (ValueError, AssertionError):
                raise  # собственное исключение
            else:
                birthdate = dt.strptime(*birthdate)
        elif isinstance(birthdate, str):
            birthdate = dt.strptime(birthdate, self._default_date_format)
        self.birthdate: date = birthdate
        self.contacts = contacts

    @property
    def fio(self):
        return self.__fio

    def change_name(
            self,
            new_name: str,
            name_part: Literal['last', 'first', 'patr']
    ):
        setattr(self, f'{name_part}_name', new_name)
        self.__fio = f'{self.last_name} {self.first_name} {self.patr_name}'

    @abstractmethod
    def __str__(self):
        pass


class Personnel(Person):

    class Degree(Enum):
        CANDIDATE = 'кандидат наук'
        DOCTOR = 'доктор наук'

    def __init__(
            self,
            last_name: str,
            first_name: str,
            patr_name: str,
            sex: Person.Sex,
            birthdate: date | str | tuple[str, str],
            contacts: Contact,
            id_: int,
            salary: dec,
            degree: Degree | None = None,
            titles: list[str] = None,
            previous_experience: dec = dec(0),
    ):
        super().__init__(
            last_name,
            first_name,
            patr_name,
            sex,
            birthdate,
            contacts
        )
        self.id = id_
        self.salary = salary
        self.degree = degree
        if titles is None:
            titles = []
        self.titles = titles
        self.job_start: date = date.today()
        self._exp = previous_experience

    @property
    def exp(self) -> dec:
        return self._exp + dec((date.today() - self.job_start).days / 365.25)


class Administrator(Personnel):
    def __str__(self):
        return f'<Administrator: {self.fio}>'


class Teacher(Personnel):
    def __init__(
            self,
            last_name: str,
            first_name: str,
            patr_name: str,
            sex: Person.Sex,
            birthdate: date | str | tuple[str, str],
            contacts: Contact,
            id_: int,
            salary: dec,
            courses: list[str],
            degree: Personnel.Degree | None = None,
            titles: list[str] = None,
            previous_experience: dec = dec(0)
    ):
        super().__init__(
            last_name,
            first_name,
            patr_name,
            sex,
            birthdate,
            contacts,
            id_,
            salary,
            degree,
            titles,
            previous_experience
        )
        self.courses = courses

    def __str__(self):
        return f'<Teacher: {self.fio}>'


class Student(Person):
    def __init__(
            self,
            last_name: str,
            first_name: str,
            patr_name: str,
            sex: Person.Sex,
            birthdate: date | str | tuple[str, str],
            contacts: Contact,
            student_id: str,
            grant: dec = dec(0),
    ):
        super().__init__(
            last_name,
            first_name,
            patr_name,
            sex,
            birthdate,
            contacts
        )
        self.student_id = student_id
        self.grant = grant

    def __str__(self):
        return f'<Student: {self.fio}>'

