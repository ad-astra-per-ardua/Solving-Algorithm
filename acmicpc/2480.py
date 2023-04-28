a,b,c = map(int,input().split())
ans = 0

if a == b == c:
    ans = 10000 + a * 1000
    print(ans)
elif a == b :
    ans = 1000 + a * 100
    print(ans)
elif b == c :
    ans = 1000 + c * 100
    print(ans)
elif a == c :
    ans = 1000 + c * 100
    print(ans)
else:
    print(max(a,b,c) * 100)