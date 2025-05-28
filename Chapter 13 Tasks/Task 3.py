import datetime


def currentDate(x):
    total_sec = datetime.timedelta(days=x).total_seconds()
    print(f"The total number of seconds is {total_sec}.")


# Student code goes here

currentDate(4)  # expected outcome: The total number of seconds is 345600.0.
currentDate(7)  # expected outcome: The total number of seconds is 604800.0.