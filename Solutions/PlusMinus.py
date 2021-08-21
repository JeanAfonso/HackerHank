#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    negative = [x for x in arr if x < 0]
    positive = [x for x in arr if x > 0]
    zero = [x for x in arr if x == 0]
    positive_div = len(positive) / len(arr)
    negative_div = len(negative) / len(arr)
    zero_div = len(zero) / len(arr)
    print(f'{positive_div:.6f}')
    print(f'{negative_div:.6f}')
    print(f'{zero_div:.6f}')


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)