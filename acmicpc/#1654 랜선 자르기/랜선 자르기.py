import sys

input = sys.stdin.readline

K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]
end = max(lan)

def length_def(n):
    count = 0
    for item in lan:
        count += item // n
    return count

def bsearch(start, end, N):
    if start > end:
        return end

    mid = (start + end) // 2
    length = length_def(mid)
    if length >= N:
        return bsearch(mid + 1, end, N)
    else:
        return bsearch(start, mid - 1, N)


print(bsearch(1, end, N))