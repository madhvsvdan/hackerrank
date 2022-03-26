#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':

    N = int(input().strip())
    my_array = []

    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()
        firstName = first_multiple_input[0]
        emailID = first_multiple_input[1]
        
        if re.search(".+@gmail\.com$", emailID):
            my_array.append(firstName)
            
    my_array.sort()
    
    for name in my_array:
        print(name)
