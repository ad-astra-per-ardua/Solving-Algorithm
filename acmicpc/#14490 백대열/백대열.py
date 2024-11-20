import sys,math
input = sys.stdin.readline

n,m = map(int,input().split(':'))
k = math.gcd(n,m)
print(f"{n//k}:{m//k}")