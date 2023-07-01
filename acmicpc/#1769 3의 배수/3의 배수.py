import sys
input = sys.stdin.readline

word = list(map(int, input().strip()))
cnt = 0

while len(word) > 1:
    cnt += 1
    temp = []
    word = sum(word)
    for i in str(word):
        temp.append(int(i))

    word = temp

print(cnt)

if word[0] % 3 == 0:
    print("YES")
else:
    print("NO")