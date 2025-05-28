from math import factorial


def calculate(x):
    result = 1
    for num in range(2, x + 1):
        result *= num
    return result

# Student code goes here



print(calculate(3))  # expected outcome: 6
print(calculate(9))  # expected outcome: 362880