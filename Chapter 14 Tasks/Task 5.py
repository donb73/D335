import os


# Complete the function to print all files in the given directory
def printFiles(someDirectory):
    files=os.listdir(someDirectory)
    for file in files:
        print(file)
    return files

# Student code goes here

# expected output: main.py
# if using PyFiddle.io otherwise it varies
printFiles(os.getcwd())
