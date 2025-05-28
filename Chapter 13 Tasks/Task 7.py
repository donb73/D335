import calendar


# Complete the function to print the full name of the month using the calendar library
def printMonthName(monthNum):
    monthNum = calendar.month_name[monthNum]
    print(monthNum)


# expected output: March
printMonthName(3)

# expected output: November
printMonthName(11)