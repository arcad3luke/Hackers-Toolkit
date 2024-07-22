#!/bin/env/python3
# This script is an attempt at the Collatz Conjecture.

def collatz_sequence(x):
    seq = [x]
    if x < 1:
       return []
    while x > 1:
       if x % 2 == 0:
         x /= 2
       else:
         x = 3 * x + 1
       seq.append(x)
    print(seq)
    return seq
