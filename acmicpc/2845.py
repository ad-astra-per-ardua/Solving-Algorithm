p, w = map(int, input().split())
a, b, c, d, e = map(int, input().split())
c = int(c)
d = int(d)
e = int(e)

ans = p * w

print(a-ans, b-ans, c-ans, d-ans, e-ans)