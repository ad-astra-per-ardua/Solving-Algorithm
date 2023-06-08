import sys,itertools
input = sys.stdin.readline

lists = []
fin = []
for _ in range(8):
    a = int(input().rstrip())
    lists.append(a)
temp = sorted(lists,reverse=True)
summation = sum(temp[0:5])


for i in temp[0:5]:
    fin.append(lists.index(i)+1)
fin.sort()
print(summation)
print(*fin)