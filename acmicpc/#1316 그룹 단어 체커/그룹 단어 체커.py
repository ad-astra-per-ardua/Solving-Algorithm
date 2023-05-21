import sys
loop = int(sys.stdin.readline().rstrip())
count = loop
for i in range(loop):
    group = sys.stdin.readline().rstrip()
    for j in range(len(group)-1):
        if group[j] == group[j+1]:
            continue
        elif group[j] in group[j+1:]:
            count -= 1
            break
print(count)