import sys
input = sys.stdin.readline

n, m = map(int,input().split())

a = set(map(int,input().split()))
b = set(map(int,input().split()))

temp1 = list(a-b)
temp2 = list(b-a)

ans = list(map(int, ' '.join(map(str,temp2)).split()))
temp1.extend(ans)
print(len(temp1))
