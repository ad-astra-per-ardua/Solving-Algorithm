import heapq,sys
input = sys.stdin.readline

k, n = map(int, input().split())
check = {}
num = list(map(int, input().split()))

q = []
heapq.heappush(q, 1)
check[1] = True
max_value = 0

while n:
    now = heapq.heappop(q)
    n -= 1

    for i in num:
        next_val = now * i

        if next_val in check:
            continue

        if len(q) > n:
            if max_value <= next_val:
                continue

        heapq.heappush(q, next_val)
        max_value = max(max_value, next_val)
        check[next_val] = True

print(q[0])
