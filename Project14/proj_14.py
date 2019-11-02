'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

- Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

import numpy as np


def collatzChainLength(x, chain):
    original_x = x
    chain_length = 1
    while x > 1:
        if x < chain.shape[0] and chain[int(x - 1)] != -1:
            chain_length += int(chain[int(x - 1)] - chain[int(0)])
            break
        chain_length += 1
        if np.mod(x, 2) == 0:
            x /= 2
        else:
            x = 3 * x + 1
    chain[original_x - 1] = chain_length
    return chain, chain_length


def collatzChain(x, chain):
    while x > 1:
        chain = np.append(chain, x)
        if np.mod(x, 2) == 0:
            x /= 2
        else:
            x = 3 * x + 1
    chain = np.append(chain, x)
    return chain


if __name__ == '__main__':
    # example check
    num = 13
    arr = np.array([])
    print(collatzChain(num, arr))

    num = 1000000
    chains_length = np.ones(num) * -1
    max_chain_num_elements = 0
    max_num = 0
    for i in range(1, num + 1):
        chains_length, chain_length = collatzChainLength(i, chains_length)
        if max_chain_num_elements < chain_length:
            max_chain_num_elements = chain_length
            max_num = i

    print("The max collatz chain is formed for:", max_num,
          "and the length of the chain is:", max_chain_num_elements)


