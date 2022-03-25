[d1, m1, y1] = [int(x) for x in input().strip().split(" ")]

[d2, m2, y2] = [int(x) for x in input().strip().split(" ")]

def date():
    if y1 > y2:
        return 10000
    elif y1 == y2:
        if m1 > m2:
            return (m1 - m2) * 500
        elif m1 == m2 and d1 > d2:
            return (d1 - d2)*15
    return 0

print(date())
