#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))

    num_swaps = 0

    for i in range(n):
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
                num_swaps += 1

        if (num_swaps == 0):
            break

    print(f'Array is sorted in {str(num_swaps)} swaps.')
    print(f'First Element: {str(a[0])}')
    print(f'Last Element: {str(a[len(a) - 1])}')
