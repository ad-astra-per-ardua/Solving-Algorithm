import sys,itertools
input = sys.stdin.readline

loop = int(input().rstrip())

lists = []
for _ in range(loop):
    a = input().split()
    lists.append(a)
lists.sort(key= lambda x: (int(x[3]), int(x[2]), int(x[1])))
print(lists[-1][0])
print(lists[0][0])