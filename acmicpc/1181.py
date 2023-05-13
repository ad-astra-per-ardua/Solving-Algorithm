import sys
loop = int(sys.stdin.readline())
lists = []

for _ in range(loop):
    lists.append(sys.stdin.readline().strip())
ans = sorted(set(lists), key=lambda x: (len(x), x))
for i in range(len(ans)):
    print(ans[i])