import datetime


# Complete the function to add 90 days to the given date and return the new date
def add90Days(someDate):
    someDate = someDate + datetime.timedelta(days=90)
    return someDate

# expected output: 2018-12-30
print(add90Days(datetime.date(2018, 10, 1)))

# expected output: 2015-05-12
print(add90Days(datetime.date(2015, 2, 11)))