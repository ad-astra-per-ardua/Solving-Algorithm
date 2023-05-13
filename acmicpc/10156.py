a,b,c = map(int, input().split())
need =(a * b) - c
if need < 0:
    need = 0
print(need)