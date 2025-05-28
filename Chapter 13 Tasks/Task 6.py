import calendar


# Complete the function to return the number of leap years in the list
def countLeapYears(yearList):
    yearList = sum(calendar.isleap(year) for year in yearList)
    return yearList

# expected output: 2
print(countLeapYears([2001, 2018, 2020, 2090, 2233, 2176, 2200, 2982]))

# expected output: 4
print(countLeapYears([2001, 2018, 2020, 2092, 2204, 2176, 2200, 2982]))