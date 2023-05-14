a, b = map(int, input().split())

y1, x1 = divmod(a-1, 4)
y2, x2 = divmod(b-1, 4)
ans = abs(y1-y2) + abs(x1-x2)
print(ans)
