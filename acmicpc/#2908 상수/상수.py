import sys
input = sys.stdin.readline

a,b = list(map(str,input().split()))
temp1 = a[::-1]
temp2 = b[::-1]

print(max(temp1,temp2))