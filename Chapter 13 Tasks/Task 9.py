import random


# Complete the following function to return a random number
# between 5 and 8 exclusive
def getRandom():
    random_number = random.randint(5, 8)
    return random_number

# expected output: You should only get 5s, 6s, and 7s
for i in range(10):
    print(getRandom())