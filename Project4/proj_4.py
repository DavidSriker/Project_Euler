'''
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

- Find the largest palindrome made from the product of two 3-digit numbers.
'''


max_num_dig = 3


def reverseInt(x):
    rev_x = 0
    while x > 0:
        rev_x *= 10
        rev_x += x % 10
        x //= 10

    return rev_x


def isPalindrome(x):
    return x == reverseInt(x)


max_val = 0
first_num = -1
second_num = -1
# Brute force method
for i in reversed(range(1, pow(10, max_num_dig))):
    for j in reversed(range(1, pow(10, max_num_dig))):
        tmp = i * j
        if (tmp > max_val and isPalindrome(tmp)):
            first_num = i
            second_num = j
            max_val = tmp
            break

print("The largest palindrome number that is a product of", max_num_dig, "is:",
      first_num, "*", second_num, "=", max_val)


# Elegant method
# P = A*B = (10^N - a)*(10^N - b)
# -> 10^2N - 10^N(a+b) + a*b
# -> 10^N*(10^N - (a+b)) + a*b
# -> 10^N*x + y; x=10^N - (a+b), y=a*b
# z = a + b
# -> 10^N*(10^N - z) + a*(z - a)
# left_side = 10^N*(10^N - z)
# right_side = reversed(left_side) = a*z - a^2
# z spanned from 2 -> 2*(9*10^N)-1 {a+b}

for z in range(2, 2 * 9 * pow(10, max_num_dig) - 1):
    left = pow(10, max_num_dig) * (pow(10, max_num_dig) - z)
    right = reverseInt(left)
    delta = pow(z, 2) - 4 * right
    if (delta > 0):
        root_1 = 0.5 * (z + pow(delta, 0.5))
        root_2 = 0.5 * (z - pow(delta, 0.5))
        if (root_1.is_integer() or root_2.is_integer()):
            first_num = pow(10, max_num_dig) - (root_1 if root_1.is_integer() else root_2)
            second_num = pow(10, max_num_dig) - (z - root_1 if root_1.is_integer() else root_2)
            max_val = first_num * second_num
            break
    else:
        continue

print("The largest palindrome number that is a product of", max_num_dig, "is:",
      first_num, "*", second_num, "=", max_val)
