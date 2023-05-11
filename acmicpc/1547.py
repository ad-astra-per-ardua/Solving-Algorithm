def switch(cups, X, Y):
    cups[X], cups[Y] = cups[Y], cups[X]
    return cups

a = int(input())
cups = [True, False, False]

for _ in range(a):
    x, y = map(int, input().split())
    cups = switch(cups, x-1, y-1)

if True in cups:
    print(cups.index(True) + 1)
else:
    print(-1)
