import math

raw = input().strip().split(' ')
a = int(raw[0])
b = int(raw[1])

raw = input().strip().split(' ')
li = []
for i in raw:
    li.append(int(i))

li.sort(reverse=True)

current = 0
cursor = 0

change = [0]
for i in range(len(li)-1):
    change.append(li[i]-li[i+1])
change.append(2000000000)

while (b > change[cursor+1]*(cursor+1)):
    current += change[cursor+1]
    b -= change[cursor+1]*(cursor+1)
    cursor += 1


print(li[0]-current-math.ceil(b/(cursor+1)))