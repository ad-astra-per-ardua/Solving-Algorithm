import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = [*map(int, input().split())]

array = [A[0]]

for item in A:
    if array[-1] < item:
        array.append(item)
    else:
        idx = bisect_left(array, item)
        array[idx] = item

print(len(array))