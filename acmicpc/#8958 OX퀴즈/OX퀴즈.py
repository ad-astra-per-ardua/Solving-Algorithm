import sys
input = sys.stdin.readline

loop = int(input())
for i in range(loop):
    count = 0
    c = 1
    lists = list(input())
    for j in lists:
        if j == 'O':
            count += c
            c += 1
        else:
            c = 1
    print(count)