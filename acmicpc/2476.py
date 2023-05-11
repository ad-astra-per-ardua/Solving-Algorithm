import sys
input = sys.stdin.readline
phase = int(input())
attempt = []
for i in range(phase):
    a, b, c = map(int,input().split())
    ans = 0
    if a == b == c:
        ans += (10000 + a * 1000)
    elif a != b and b != c and a != c:
        ans += max(a,b,c)*100
    else:
        if a == b:
            ans += 1000 + a * 100
        elif b == c:
            ans += 1000 + b * 100
        elif a == c:
            ans += 1000 + c * 100
    attempt.append(ans)
attempt.sort()
print(max(attempt))
