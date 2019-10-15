'''
Project Number 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

- Find the sum of all the multiples of 3 or 5 below 1000.

'''

import numpy as np

max_val = 1000

vec = np.linspace(1, max_val - 1, max_val - 1, dtype=np.int32)
mult_3 = 3 * vec
mult_5 = 5 * vec
intersection = np.intersect1d(mult_3, mult_5)

mult_3 = mult_3[np.where(mult_3 < max_val)]
mult_5 = mult_5[np.where(mult_5 < max_val)]
intersection = intersection[np.where(intersection < max_val)]

total_sum = 0.0
total_sum += np.sum(mult_3)
total_sum += np.sum(mult_5)
# subtract all the repetitions
total_sum -= np.sum(intersection)

print("The sum of all the multiples of 3 or 5 below",  max_val, "is: ", total_sum)



