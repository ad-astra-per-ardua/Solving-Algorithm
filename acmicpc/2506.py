a = int(input())
ans = []
score = 0
temp2 = 0
while True:
    if len(ans) == a:
        break
    ans = list(map(int,input().split()))
for i in range(0,a):
    if ans[i] == 1:
        temp2 += 1
        score += temp2
    else:
        temp2 = 0
print(score)