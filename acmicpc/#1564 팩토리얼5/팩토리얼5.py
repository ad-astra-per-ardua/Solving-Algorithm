import sys
input = sys.stdin.readline
s=1
n=int(input())
for i in range(1,n+1):
    s*=i
    s=int(str(s).rstrip("0")[-12:])
print(str(s)[-5:])