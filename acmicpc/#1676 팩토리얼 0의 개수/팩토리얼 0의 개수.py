import math,sys
input = sys.stdin.readline
a = int(input())

temp = list(str(math.factorial(a)))
temp.reverse()
if temp[0] == '0':
    for i in range(1,len(temp)-1):
        if temp[i-1] != temp[i]:
            break
else:
    print(0)
    sys.exit(0)

print(i)
