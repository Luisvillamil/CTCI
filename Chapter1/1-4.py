#1-4 Palindrome Permutation
# Similar problem in Hackerrank: https://www.hackerrank.com/challenges/game-of-thrones/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    freq = {}
    for x in s:
        if x in freq:
            freq[x]+=1
        else:
            freq[x] = 1
    count = 0
    for x in freq:
        if freq[x]%2 == 1:
            count += 1
        if count > 1:
            return "NO"
    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()


#Pythonian way:
def gameOfThrones(s):
    return (sum(s.count(x)%2 for x in set(s) ) <2  and 'YES') or 'NO'
