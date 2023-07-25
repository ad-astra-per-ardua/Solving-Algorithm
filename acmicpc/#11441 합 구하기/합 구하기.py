import sys
input = sys.stdin.readline

n = int(input())
array_n = list(map(int,input().split()))
prefix_sum = [0] * (n + 1)

for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + array_n[i - 1]

m = int(input())
for _ in range(m):
    i, j = map(int,input().split())
    print(prefix_sum[j] - prefix_sum[i - 1])
