import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    D = [[False] * 7 for _ in range(N + 1)]
    D[0][1] = True

    for i in range(1, N + 1):
        ops = input().split()
        for x in range(7):
            if D[i - 1][x]:
                for j in range(1, 4, 2):
                    val = int(ops[j])
                    D[i][(x + val) % 7 if ops[j-1] == '+' else (x * val) % 7] = True

    print("LUCKY" if D[N][0] else "UNLUCKY")
