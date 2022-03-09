result, maximum = 0, 0

while n > 0:
    if n % 2 == 1:
        result += 1
        if result > maximum:
            maximum = result
    else:
        result = 0
    n //= 2

print(maximum)
