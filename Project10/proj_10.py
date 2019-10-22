'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

- Find the sum of all the primes below two million.
'''

def sieveOfEratosthenesMethod(N):
    # following:
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    # initiate an array of True boolean of size N
    bool_vec = [True for i in range(N + 1)]
    bool_vec[0] = False
    bool_vec[1] = False
    prime = 2

    while (pow(prime, 2) <= N):
        if bool_vec[prime]:
            # update all multiple of prime
            for idx in range(pow(prime, 2), N + 1, prime):
                bool_vec[idx] = False
        prime += 1
    return [idx for idx, bool_val in enumerate(bool_vec) if bool_val]


max_val = 2000000
s = sum(sieveOfEratosthenesMethod(max_val))
print("The sum of all the prime numbers below", max_val,
      "is", s)