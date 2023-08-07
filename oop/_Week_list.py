from datetime import datetime as dt, date, timedelta as td


class Week(list):
    _default_date_format = '%d.%m.%Y'
    weekdays = ('Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс')

    def __init__(self, new_date: date | str = None):
        if new_date is None:
            new_date = date.today()
        self.today = new_date

    @property
    def today(self) -> str:
        return self._today_str

    # list изменяемый тип, поэтому изменяющий сеттер допустим
    @today.setter
    def today(self, new_date: date | str | tuple[str, str]):
        if isinstance(new_date, str):
            new_date = dt.strptime(new_date, self._default_date_format).date()
        elif isinstance(new_date, tuple):
            new_date, format = new_date
            new_date = dt.strptime(new_date, format).date()
        self._today = new_date
        self._today_str = f'{self._today:{self._default_date_format}}'
        self.clear()
        self.extend(
            self._today + td(days=i-self._today.weekday())
            for i in range(7)
        )

    def __str__(self):
        weekdays = ' '.join(self.weekdays)
        days = ' '.join(f'{day.day:>2}' for day in self)
        return f'{weekdays}\n{days}'

