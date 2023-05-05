f = int(input())
li = []
for i in range(f):
    a = int(input())
    li.append(a)

list(set(li))
li.sort()

for loop in li:
    print(loop)