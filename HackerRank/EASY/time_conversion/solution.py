#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'timeConversion' function below.
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.


def timeConversion(s: str) -> str:
    # Write your code here
    if s.endswith("AM"):
        return s.replace("AM", '')
    s = s.replace("PM", '')
    result: list[int] = [int(x) for x in s.split(':')]
    result[0] += 12
    return ':'.join([str(x) for x in result])


if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    fptr.write(result + '\n')
    fptr.close()

# eosc