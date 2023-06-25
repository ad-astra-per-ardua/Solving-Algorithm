import sys
input = sys.stdin.readline

loop = int(input().rstrip())

for i in range(loop):
    m = int(input().rstrip())
    a = b = 0
    c = 1 << 61
    for y in range(60):
        for x in range(y + 1):
            t = abs((1 << x) + (1 << y) - m)
            if t < c:
                c = t
                a = x
                b = y
    print(a, b)
