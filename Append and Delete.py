#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    c=0
    l = len(s)
    while s[:l]!=t[:l]:
        l-=1
        c+=1
    o = ((len(t)-l)+c)
    if k<o:
        return "No"
    elif (len(s)+len(t))<=k:
        return "Yes"
    elif 2*len(t)<k:
        return "Yes"
    elif k%2 == o%2:
        return "Yes"
    else:
        return "No"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
