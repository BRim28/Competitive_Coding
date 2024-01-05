'''
Link: https://www.hackerrank.com/challenges/reduced-string/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
Venue: Hackerrank
Date: 05 Jan 2024
Description: Reduce given string to smallest possible with no adjacent repeating characters
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    # Write your code here
    changed = True
    while changed:
        i = 0
        changed = False
        len_s = len(s)
        while i<len_s-1:
            if s[i]==s[i+1]:
                s = s[:i]+s[i+2:]
                changed = True
                len_s-=2
            i+=1
    if s:
        return s
    else:
        return "Empty String"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
