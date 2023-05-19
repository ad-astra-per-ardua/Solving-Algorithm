import sys
input = sys.stdin.readline
a,b = map(int, input().split())
n = list(map(int, input().split()))
m = list(map(int, input().split()))

sum_array = n + m
sum_array.sort()

print(' '.join(map(str, sum_array)))