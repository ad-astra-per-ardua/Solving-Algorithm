res = []
for i in range(9):
    a = int(input())
    res.append(a)
ans = max(res)
print(ans)
print(res.index(ans) + 1)
