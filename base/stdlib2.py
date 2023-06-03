from datetime import datetime as dt, timezone as tz, timedelta as td


current_datetime = dt.now()
print(current_datetime)

components = (
    current_datetime.year,
    current_datetime.month,
    current_datetime.day,
    current_datetime.hour,
    current_datetime.minute,
    current_datetime.second,
    current_datetime.microsecond,
)
print(*components, sep='\n', end='\n\n')

print(f'{current_datetime:%H.%M}')
print(f'{current_datetime:%d.%m.%y}')
print(f'{current_datetime:%d/%m/%Y}\n')

# while True:
    # inp = input('введите дату в формате дд.мм.гггг: ')
    # if not inp:
        # break
    # dt_from_inp = dt.strptime(inp, '%d.%m.%Y')
    # print(repr(dt_from_inp))


offset = tz(td(hours=5))
dt_tz = dt(year=2023, month=6, day=3, hour=15, minute=0)#, tzinfo=offset)
print(dt_tz)


td1 = dt_tz - current_datetime
print(td1)
