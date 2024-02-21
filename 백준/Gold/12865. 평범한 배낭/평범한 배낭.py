import sys
input = sys.stdin.readline

n,k = map(int, input().split())
put = [[1, 1]]
bag = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for _ in range(n):
    put.append(list(map(int, input().split())))

for i in range(1, n + 1):
    for j in range(1, k + 1):
        kg = put[i][0]
        val = put[i][1]

        if j < kg:
            bag[i][j] = bag[i - 1][j]
        else:
            bag[i][j] = max(val + bag[i - 1][j - kg], bag[i - 1][j])

print(bag[n][k])