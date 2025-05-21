# Complete the function to return the number of uppercase letters in the given string
def countUpper(mystring):
    return sum(1 for char in mystring if char.isupper())



# expected output: 4
print(countUpper('Welcome to WGU'))

# expected output: 2
print(countUpper('Hello, Mary'))