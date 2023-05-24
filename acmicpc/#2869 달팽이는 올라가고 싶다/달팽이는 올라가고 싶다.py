import math
a, b, v = map(int,input().split())
if b >= a:
    exit()
day = 0
v -= a 
day += 1
day += math.ceil(v / (a - b))

print(day)