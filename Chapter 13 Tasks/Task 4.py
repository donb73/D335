import datetime as dt


def currentDate():
    c_d = dt.datetime.now()
    current_date = f"{c_d.month}-{c_d.day}-{c_d.year}"
    return current_date

print(currentDate())  # Expected outcome will vary, but should follow this format: The current date is 9-11-2018.