from collections import deque
l = deque([0,1])
a = int(input())
for i in range(2,a+1):
    l.append(l[i-2] + l[i-1])

print(l[-1])