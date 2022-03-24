from math import sqrt

T = int(input())

def check_prime(n):
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

for i in range(T):
    n = int(input())
    if n >= 2 and check_prime(n):
        print("Prime")
    else:
        print("Not prime")
