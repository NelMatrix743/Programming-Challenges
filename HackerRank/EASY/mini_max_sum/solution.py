#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'miniMaxSum' function below.
# The function accepts INTEGER_ARRAY arr as parameter.

def miniMaxSum(arr):
    minresult: int = sum(sorted(arr)[0:4])
    maxresult: int = sum(sorted(arr)[1:])
    print(minresult, maxresult)


if __name__ == '__main__':

    arr: list[int] = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)

# eosc