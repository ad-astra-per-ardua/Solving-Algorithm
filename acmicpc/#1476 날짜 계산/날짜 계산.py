import sys
input = sys.stdin.readline
e, s, m = map(int,input().split())
x = 1
while True:
    if x % 15 == e % 15 and x % 28 == s % 28 and x % 19 == m % 19:
        print(x)
        break
    x += 1