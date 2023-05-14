import sys

loop = int(input())
lists = []
for _ in range(loop):
    lists.append(int(sys.stdin.readline().strip()))
lists.sort()
for i in lists:
    print(i)