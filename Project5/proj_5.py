'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

- What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

from functools import reduce

max_divisor = 20


def isNumEvenlyDivisible(x, div):
    return (x % div) == 0


def isNumEvenlyDivisibleByRange(x, max_div):
    flag = True
    for i in range(1, max_div + 1):
        flag = flag and isNumEvenlyDivisible(x, i)

    return flag


def gcd(x1, x2):
    # using Euclid's algorithm
    while x2:
        x1, x2 = x2, x1 % x2

    return x1


def lcm(x1, x2):
    # from the web:
    # https://en.wikipedia.org/wiki/Least_common_multiple
    return abs(x1 * x2) / gcd(x1, x2)


# Brute force approach - slowly!
num = 0
found_num = False
while not found_num:
    num += 1
    found_num = isNumEvenlyDivisibleByRange(num, max_divisor)

print("The smallest positive number that is evenly divisible by all of the numbers from 1 to", max_divisor,
      "is:", num)

# Elegant solution
# option 1: using a loop
res = 0
for i in range(2, max_divisor + 1):
    if i == 2:
        res = lcm(i - 1, i)
    else:
        res = lcm(res, i)

print("The smallest positive number that is evenly divisible by all of the numbers from 1 to", max_divisor,
      "is:", res)

# option 2: using reduce()
res = 0
print("The smallest positive number that is evenly divisible by all of the numbers from 1 to", max_divisor,
      "is:", reduce(lcm, range(1, max_divisor + 1)))
