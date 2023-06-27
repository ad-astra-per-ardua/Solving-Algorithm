import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

def solve(depth, idx, n, m):
    if depth == m:
        temp = ' '.join(map(str, result))
        if temp not in result_set:
            result_set.add(temp)
            print(temp)
        return
    for i in range(idx, n):
        result.append(numbers[i])
        solve(depth + 1, i, n, m)
        result.pop()

result = []
result_set = set()
solve(0, 0, n, m)
