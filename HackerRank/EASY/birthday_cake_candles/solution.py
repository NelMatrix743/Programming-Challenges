#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'birthdayCakeCandles' function below.
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.


def birthdayCakeCandles(candles: int, size: int) -> int:
    return candles.count(max(candles))
  

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles, candles_count)
    fptr.write(str(result) + '\n')
    fptr.close()

# eosc