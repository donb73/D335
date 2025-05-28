from math import e, ceil


def mathCalculation(x):
    x = x * e
    x = ceil(x)
    return x

# expected outcome: 9
print(mathCalculation(3))

# expected outcome: 25
print(mathCalculation(9))