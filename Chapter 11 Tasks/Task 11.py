# Complete the function to remove a dictionary item if it exists
def removeDictItem(mydict, key):
    mydict.pop(key) if key in mydict else "Not Found"
    return mydict

# Student code goes here

# expected output: {'tomato': 'red', 'lime': 'green'}
print(removeDictItem({'tomato': 'red', 'banana': 'yellow', 'lime': 'green'}, 'banana'))

# expected output: {'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'}
print(removeDictItem({'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'}, 'Cameroon'))