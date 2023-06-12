import sys
input = sys.stdin.readline

lists = []
n = int(input())
for _ in range(n):
    a = int(input())
    lists.append(a)
lists = sorted(lists,reverse=True)

for i in range(len(lists)-2):
    if lists[i] < lists[i+1] + lists[i+2]:
        print(lists[i] + lists[i+1] + lists[i+2])
        break
else:
    print(-1)

