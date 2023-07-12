import sys
input = sys.stdin.readline

loop = int(input().rstrip())
num = list(map(int,input().split()))
count = 0
ans = 0
random = []

for i in num:
    if i not in random:
        random.append(i)
        count += 1
    elif i in random:
        count -= 1
    ans = max(ans, count)
print(ans)
