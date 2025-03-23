# LeetCode-Daily
Going up the LeetCode world day by day

## number to binary in f string

f"{int(a):b}" for a in nums 

## fill with zeros

"789".zfill(5) ----> "00789"

## mod tricks

add 26 for alphabets-num...mod 26

## count no of 1 bits in binary representation (num is integer)

num.bit_count()

## Flipping bits

num & (1 << i)        Check if the i-th bit is set
num & (1 << i) == 0   Check if i-th bit is unset
num ^= (1 << i)       flip 1 to 0
num |= (1 << i)       flip 0 to 1

## functools reduce

from functools import reduce
from operator import xor
res = reduce(xor,list)  performs XOR operation of all list elements



