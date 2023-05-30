import sys
input = sys.stdin.readline
strings, loop = map(int,input().split())
box = []
pics = []
count = 0
for _ in range(loop):
    a, b = map(int, input().split())
    box.append(a)
    pics.append(b)

box.sort()
pics.sort()

if box[0] > pics[0] * 6:
    count += strings * pics[0]
else:
    count += (strings // 6) * box[0]
    if (strings % 6)*pics[0] > box[0]:
        count += box[0]
    else:
        count += (strings % 6)*pics[0]
print(count)
