'''
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is:
3025 − 385 = 2640.

- Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

num_elem = 100

# sum(i) from 1->N is N*(N+1)/2
# sum(i^2) from 1->N is N*(N+1)*(2*N+1)/6

sum_x = (num_elem * (num_elem + 1)) / 2
sum_x_squared = (num_elem * (num_elem + 1) * (2 * num_elem + 1)) / 6
print("sum(x)^2 from 1 ->", num_elem, " =", pow(sum_x, 2))
print("sum(x^2) from 1 ->", num_elem, " =", sum_x_squared)
print("sum(x)^2 - sum(x^2) =", pow(sum_x, 2), "-", sum_x_squared, "=", pow(sum_x, 2) - sum_x_squared)
