import sys
input = sys.stdin.readline
def switch(a,b,box):
    temp = box[a-1]
    box[a-1] = box[b-1]
    box[b-1] = temp

    return box


n, m = map(int, input().split())

box = [*range(1,101)]
for _ in range(m):
    x,y = map(int, input().split())
    box = switch(x,y,box)



print(*box[0:n])