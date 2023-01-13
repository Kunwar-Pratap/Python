import calendar

html_calendar = calendar.HTMLCalendar(firstweekday=0)
year = 2023
month = 1
print(html_calendar.formatmonth(year, month))