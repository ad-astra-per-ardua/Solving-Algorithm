import sys
input = sys.stdin.readline

n,m = map(int,input().split())
id = {}
char = {}
for i in range(1, n+1):
    poke = input().rstrip()
    id[i] = poke
    char[poke] = i
for _ in range(m):
    t = input().rstrip()
    if t.isdigit():
        print(id[int(t)])
    else:
        print(char[t])