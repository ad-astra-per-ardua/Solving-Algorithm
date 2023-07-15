import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int,input().split()))
sa = sorted(array)
ans = [0] * n
for i in range(n):
    idx = sa.index(array[i])
    ans[i] = idx
    sa[idx] = -1

print(*ans)