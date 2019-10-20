'''
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

- Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
- What is the value of this product?
'''

seq = "73167176531330624919225119674426574742355349194934" \
      "96983520312774506326239578318016984801869478851843" \
      "85861560789112949495459501737958331952853208805511" \
      "12540698747158523863050715693290963295227443043557" \
      "66896648950445244523161731856403098711121722383113" \
      "62229893423380308135336276614282806444486645238749" \
      "30358907296290491560440772390713810515859307960866" \
      "70172427121883998797908792274921901699720888093776" \
      "65727333001053367881220235421809751254540594752243" \
      "52584907711670556013604839586446706324415722155397" \
      "53697817977846174064955149290862569321978468622482" \
      "83972241375657056057490261407972968652414535100474" \
      "82166370484403199890008895243450658541227588666881" \
      "16427171479924442928230863465674813919123162824586" \
      "17866458359124566529476545682848912883142607690042" \
      "24219022671055626321111109370544217506941658960408" \
      "07198403850962455444362981230987879927244284909188" \
      "84580156166097919133875499200524063689912560717606" \
      "05886116467109405077541002256983155200055935729725" \
      "71636269561882670428252483600823257530420752963450"


def retrieveDigits(idx, s_size):
    return int(seq[idx - s_size]), int(seq[idx])


def stringNumProduct(s):
    prod = 1
    for i in range(len(s)):
        prod *= int(s[i])
    return prod


def updateProduct(prev_prod, numerator, denominator):
    return (prev_prod * numerator) / denominator


def containZero(s):
    return '0' in s


def findSubSeqWithoutZero(sub_seq, size, prev, new):
    while True:
        if containZero(sub_seq):
            prev += size
            new += size
            try:
                sub_seq = seq[prev:new]
            except:
                return -1, -1
        else:
            break
    return prev, new


size_of_sub_seq = 13
prev_pos = 0
new_pos = prev_pos + size_of_sub_seq
sub_seq = seq[prev_pos:new_pos]
# avoid zeros on the starting sub-string
prev_pos, new_pos = findSubSeqWithoutZero(sub_seq, size_of_sub_seq,
                                          prev_pos, new_pos)

max_res = 0
curr_res = 0
max_seq = sub_seq
recalculate = True

while True:
    if recalculate:
        curr_res = stringNumProduct(sub_seq)
        recalculate = False
    else:
        curr_res = updateProduct(curr_res, curr_new_digit, prev_start_digit)

    max_seq = sub_seq if curr_res > max_res else max_seq
    max_res = curr_res if curr_res > max_res else max_res

    try:
        prev_start_digit, curr_new_digit = retrieveDigits(new_pos, size_of_sub_seq)
        prev_pos += 1
        new_pos += 1
        sub_seq = seq[prev_pos:new_pos]
        if curr_new_digit == 0:
            recalculate = True
            prev_pos, new_pos = findSubSeqWithoutZero(seq[prev_pos:new_pos], size_of_sub_seq,
                                                      prev_pos, new_pos)
            if prev_pos == -1:
                print("End of series reached")
                break
            sub_seq = seq[prev_pos:new_pos]
    except:
        print("End of series reached")
        break


print("The max product sub sequence of size:", size_of_sub_seq, "is:", max_seq)
print("The result of the product is:")
for i in range(size_of_sub_seq):
    if i == size_of_sub_seq - 1:
        print(max_seq[i], "=", max_res)
    else:
        print(max_seq[i], "* ", end='')








