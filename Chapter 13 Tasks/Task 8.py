import calendar, datetime


# Complete the function to print the full name of the day of the week
def printWeekdayName(year, month, day):
    date = datetime.date(year, month, day)
    num_day = date.weekday()
    weekday_n = calendar.day_name[num_day]
    print(weekday_n)


# expected output: Friday
printWeekdayName(2001, 8, 31)

# expected output: Monday
printWeekdayName(2018, 10, 1)