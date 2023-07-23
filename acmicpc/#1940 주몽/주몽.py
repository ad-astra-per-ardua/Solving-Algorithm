import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
matr = list(map(int, input().split()))
matr.sort()

start, end = 0, n-1
count = 0

while start < end:
    if matr[start] + matr[end] == m:
        count += 1
        start += 1
        end -= 1
    elif matr[start] + matr[end] > m:
        end -= 1
    else:
        start += 1

print(count)
