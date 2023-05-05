n = int(input())

ans = [[0, 0] for _ in range(1001)]

ans[0][0] = 0
ans[0][1] = 1
ans[1][0] = 0
ans[1][1] = 1
ans[2][0] = 1
ans[2][1] = 0
ans[3][0] = 0
ans[3][1] = 0
ans[4][0] = 2
ans[4][1] = 1

for i in range(3, n + 1):
    gs = set()
    for j in range(i - 1):
        gs.add(ans[i - 2 - j][0] ^ ans[j][0])
    for j in range(i):
        if not j in gs:
            ans[i][0] = j
            break

print(1 if ans[n][0] != 0 else 2)
