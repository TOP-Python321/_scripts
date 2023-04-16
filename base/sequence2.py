current_day = 16
current_month = 4
current_year = 2023

inp = input(' введите дату рождения в формате ДД.ММ.ГГГГ: ')

if len(inp) == 10:
    day = inp[:2]
    month = inp[3:5]
    year = inp[6:]
    
    if day.isdecimal() and month.isdecimal() and year.isdecimal():
        day = int(day)
        month = int(month)
        year = int(year)
        
        days_gone = (
            (current_year - year)*365 
            + (current_month - 1)*30 + current_day 
            + (12 - month)*30 - day 
        )
        print(f'вы прожили примерно {days_gone} дней')
