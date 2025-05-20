# Complete the function to order the values in the list
# if ascending is true then order lowest to highest
# if ascending is false then order highest to lowest
def sortList(mylist, ascending):
    return sorted(mylist, reverse=not ascending)

# Student code goes here

# expected output: [4, 12, 19, 33]
print(sortList([19, 4, 33, 12], True))

# expected output: [33, 19, 12, 4]
print(sortList([19, 4, 33, 12], False))