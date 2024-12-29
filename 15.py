import calendar

# Вывести календарь на 2024 год
print(calendar.calendar(2024))

# Вывести календарь на октябрь 2024
print(calendar.month(2024, 10))

# Какой день недели был 1 января 2024?
weekday = calendar.weekday(2024, 1, 1)
print(f"1 января 2024 был {calendar.day_name[weekday]}") # day_name - список названий дней недели

# Високосный ли 2024 год?
is_leap = calendar.isleap(2024)
print(f"2024 год {'високосный' if is_leap else 'не високосный'}")

# Календарь на месяц в виде списка списков
month_calendar = calendar.monthcalendar(2024, 10)
print(month_calendar)

# Создание HTML календаря
html_calendar = calendar.HTMLCalendar()
print(html_calendar.formatyear(2024))