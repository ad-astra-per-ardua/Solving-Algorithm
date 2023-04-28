import sys

input = sys.stdin.readline


def init(start, end, node):
    if start == end:
        tree[node] = nums[start]
    else:
        mid = (start + end) // 2
        init(start, mid, node * 2)
        init(mid + 1, end, node * 2 + 1)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]


def query(start, end, node, left, right):
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return query(start, mid, node * 2, left, right) + query(mid + 1, end, node * 2 + 1, left, right)


def update(start, end, node, index, diff):
    if index < start or end < index:
        return
    tree[node] += diff
    if start != end:
        mid = (start + end) // 2
        update(start, mid, node * 2, index, diff)
        update(mid + 1, end, node * 2 + 1, index, diff)


n, q = map(int, input().split())
nums = list(map(int, input().split()))

tree = [0] * (n * 4)
init(0, n - 1, 1)

for _ in range(q):
    x, y, a, b = map(int, input().split())

    if x > y:
        x, y = y, x

    print(query(0, n - 1, 1, x - 1, y - 1))

    diff = b - nums[a - 1]
    nums[a - 1] = b
    update(0, n - 1, 1, a - 1, diff)
