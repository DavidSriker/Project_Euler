'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

- What is the 10001st prime number?
'''

import numpy as np


def isPrime(x):
    if x <= 1:
        return False
    if x == 2:  # 2 is prime number
        return True
    if x % 2 == 0:  # if the number is even is not prime
        return False

    prime = 3
    while (prime < pow(x, 0.5) + 1):
        if x % prime == 0:
            return False
        else:
            prime += 2  # all the rest of primes are odd
    # if we got here -> we could not find a divisor
    return True


# Brute force
prime_index = 10001
idx = 0
num_iterator = 2
n_prime = -1
while (idx < prime_index):
    if isPrime(num_iterator):
        idx += 1
        n_prime = num_iterator
    num_iterator += 1

print("The", prime_index, "prime number is:", n_prime)

# Elegant way - check only division in the known primes
prime_index = 10001
idx = 1
num_iterator = 3
prime_factors_vec = np.array([2])
while (idx < prime_index):
    prime_flag = True
    for elem_idx in np.where(prime_factors_vec <= pow(num_iterator, 0.5))[0]:
        if (num_iterator % prime_factors_vec[elem_idx] == 0):
            prime_flag = False
            break
    if prime_flag:
        prime_factors_vec = np.append(prime_factors_vec, num_iterator)
        idx += 1
    num_iterator += 1

print("The", prime_index, "prime number is:", prime_factors_vec[-1])


