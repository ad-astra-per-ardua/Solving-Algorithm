import sys

input = sys.stdin.readline

def solve():
    n = int(input())
    selected = [0] + list(map(int, input().split()))
    visited = [0] * (n + 1)
    team = 0
    for i in range(1, n+1):
        if visited[i] == 0:
            cycle = [i]
            visited[i] = 1
            while True:
                nxt = selected[cycle[-1]]
                if visited[nxt] == 0:
                    visited[nxt] = 1
                    cycle.append(nxt)
                elif visited[nxt] == 1 and nxt in cycle:
                    team += len(cycle[cycle.index(nxt):])
                    break
                else:
                    break
    print(n - team)

t = int(input())
for _ in range(t):
    solve()
