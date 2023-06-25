import sys
input = sys.stdin.readline

n = int(input())

list_X = []

for i in range(1, n + 1):
    if i ** 2 > n:
        break
    if n % i == 0:
        list_X.append(i)
        list_X.append(n // i)

list_Y = []

for i in range(1, n + 3):
    if i ** 2 > n + 2:
        break
    if (n + 2) % i == 0:
        list_Y.append(i)
        list_Y.append((n + 2) // i)
for a in list_X:
    for b in list_Y:
        c = n // a
        d = -(n + 2) // b
        if a * d + b * c == n + 1:
            print(a, b, c, d)
            exit(0)
print(-1)
