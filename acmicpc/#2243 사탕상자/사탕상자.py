import sys
input = sys.stdin.readline

MAX_N = 1000000
tree = [0] * (MAX_N * 4)

def update(node, start, end, index, diff):
    if index < start or index > end:
        return
    tree[node] += diff
    if start != end:
        mid = (start + end) // 2
        update(node * 2, start, mid, index, diff)
        update(node * 2 + 1, mid + 1, end, index, diff)

def query(node, start, end, count):
    if start == end:
        return start
    mid = (start + end) // 2
    if tree[node * 2] >= count:
        return query(node * 2, start, mid, count)
    else:
        return query(node * 2 + 1, mid + 1, end, count - tree[node * 2])

n = int(input())
for _ in range(n):
    data = list(map(int, input().split()))
    if data[0] == 1:
        rank = data[1]
        candy = query(1, 1, MAX_N, rank)
        print(candy)
        update(1, 1, MAX_N, candy, -1)
    else:
        flavor = data[1]
        count = data[2]
        update(1, 1, MAX_N, flavor, count)
