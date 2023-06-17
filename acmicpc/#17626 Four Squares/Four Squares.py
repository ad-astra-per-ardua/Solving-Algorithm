import sys
input = sys.stdin.readline
n = int(input())
array = [0 if i ** 0.5 % 1 else 1 for i in range(n + 1)]

minimum = 4
for i in range(int(n ** 0.5), 0, -1):
    if array[n]:
        minimum = 1
        break
    elif array[n - i ** 2]:
        minimum = 2
        break
    else:
        for j in range(int((n - i ** 2) ** 0.5), 0, -1):
            if array[(n - i ** 2) - j ** 2]:
                minimum = 3
print(minimum)
