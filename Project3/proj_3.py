'''
Project Number 3

The prime factors of 13195 are 5, 7, 13 and 29.

- What is the largest prime factor of the number 600851475143 ?

'''

import numpy as np

N_original = 600851475143
N = N_original

prime = 2
prime_vec = np.array([])

while N > prime:
    if (N % prime == 0):
        N /= prime
        prime_vec = np.append(prime_vec, prime)
        prime = 2
    else:
        prime += 1

prime_vec = np.append(prime_vec, prime)

unique_primes = np.unique(prime_vec)
for i in range(len(unique_primes)):
    p = unique_primes[i]
    rep_amount = len(np.where(prime_vec == p)[0])
    if (i == len(unique_primes) - 1):
        print(p, "^", rep_amount, " = ", N_original,  sep="")
    else:
        print(p, "^", rep_amount, " * ", sep="", end="")

print("The maximal prime factor is:", np.max(unique_primes))




