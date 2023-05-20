import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(A)
    C = defaultdict(int)
    C[A[0]] += 1
    C[A[-1]] += 1
    for a in A[1:-1]:
        C[a] += 2
    ans = -1
    for i in range(1, A[-1] - A[0] + 1):
        if C[i] == 0:
            ans = i
            break
    if ans == -1:
        print(-1)
    else:
        print(ans)

if __name__ == "__main__":
    main()
