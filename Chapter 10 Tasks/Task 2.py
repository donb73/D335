# Complete the function to return the last X number of characters
# in the given string
def getLast(mystring, x):
    return mystring[len(mystring) - x:]

# Student code goes here

# expected output: IT
print(getLast('WGU College of IT', 2))

# expected output: College of IT
print(getLast('WGU College of IT', 13))