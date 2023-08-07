from datetime import datetime as dt, date, timedelta as td


class Week(tuple):
    _default_date_format = '%d.%m.%Y'
    weekdays = ('Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс')

    # вся работа по генерации неизменяемого объекта должна быть проведена в __new__() потому что другой возможности для этого не будет
    def __new__(cls, new_date: date | str | tuple[str, str] = None):
        if new_date is None:
            new_date = date.today()
        elif isinstance(new_date, str):
            new_date = dt.strptime(new_date, cls._default_date_format).date()
        elif isinstance(new_date, tuple):
            new_date, date_format = new_date
            new_date = dt.strptime(new_date, date_format).date()
        else:
            raise TypeError

        instance = super().__new__(
            cls,
            (new_date + td(days=i-new_date.weekday())
             for i in range(7))
        )
        instance._today_str = f'{new_date:{cls._default_date_format}}'
        return instance

    @property
    def today(self) -> str:
        return self._today_str

    # неизменяемый тип, поэтому изменяющий сеттер недопустим (а пересоздающий не будет работать)
    @today.setter
    def today(self, new_date: date | str | tuple[str, str]):
        raise TypeError(f'{self.__class__.__name__!r} object does not support day assignment')

        # проблема была в том, что self является локальной переменной, поэтому её пересоздание не имеет смысла — интерпретатор переключается на локальное пространство имён
        # self = self.__class__(
        #     self._today + td(days=i-self._today.weekday())
        #     for i in range(7)
        # )

    def __str__(self):
        weekdays = ' '.join(self.weekdays)
        days = ' '.join(f'{day.day:>2}' for day in self)
        return f'{weekdays}\n{days}'

