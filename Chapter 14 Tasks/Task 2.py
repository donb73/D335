import os


# Complete the function to return the directory name only from the given file name
def getDirectoryName(fileName):
    return os.path.split(fileName)[0]

# expected output: /var/www
print(getDirectoryName("/var/www/test.html"))

# expected output: /var/www/apple
print(getDirectoryName("/var/www/apple/test.html"))
