import sys
a = int(sys.stdin.readline().strip())
ans = 1
if a == 1:
    print('1')
else:
    for i in range(a):
        ans += 6 * i
        if ans >= a:
            break
    print(i+1)