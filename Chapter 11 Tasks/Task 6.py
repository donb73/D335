# Complete the function to remove the first item in the given list
def removeFirst(mylist):
    mylist.pop(0)
    return mylist

# Student code goes here

# expected output: [7, 8, 9]
print(removeFirst([6, 7, 8, 9]))

# expected output: [2, 3, 4]
print(removeFirst([1, 2, 3, 4]))