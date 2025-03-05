#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'compare_triplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b

# Using if-elif
def compare_triplets(a: list[int], b: list[int]) -> list[int]:
    a_score = b_score = 0
    for idx in range(len(a)):
        if a[idx] > b[idx]: 
            a_score += 1
            continue
        elif a[idx] < b[idx]:
            b_score += 1
    return [a_score, b_score]


# Using structural pattern matching (match-statement, Python 3.10 and above)
# def compare_triplets(a: list[int], b: list[int]) -> list[int]:
#     a_score = b_score = 0
#     for idx in range(len(a)):
#         match (a[idx], b[idx]):
#             case (x, y) if x > y:
#                 a_score += 1
#             case (x, y) if x < y:
#                 b_score += 1
#     return [a_score, b_score]


if __name__ == '__main__':

    print("<input>")

    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    result = compare_triplets(a, b)
    print(result)

# eosc