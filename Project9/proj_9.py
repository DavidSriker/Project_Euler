'''
A Pythagorean triplet is a set of three natural numbers, a < b < c,
for which, a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.

- Find the product abc.
'''

for b in range(1, 1000):
    a = 500 * ((1000 - 2 * b)/(1000 - b))
    if (a == int(a)):
        c = 1000 - a - b
        print("a =", a, ", b =", b, ", c =", c)
        print("The sum of a,b,c is:", a + b + c)
        print("The product of a,b,c is:", a * b * c)
        break



