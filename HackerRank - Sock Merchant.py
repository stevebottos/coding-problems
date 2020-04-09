#!/bin/python3

import math
import os
import random
import re
import sys


# For debugging
def printOut(a):
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write(str(ar))

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    
    # check to name sure that the array is >1 elements first
    if len(ar) <= 1:
        return 0
    
    ar_uniques = set(ar)
    
    number_of_pairs = 0
    for unique in ar_uniques:
        number_of_instances = ar.count(unique)
        if number_of_instances > 2:
            number_of_pairs += int(number_of_instances/2)
        elif number_of_instances == 2:
            number_of_pairs += 1
        
    return number_of_pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()