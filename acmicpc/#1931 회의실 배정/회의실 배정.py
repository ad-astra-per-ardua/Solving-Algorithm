import sys
input = sys.stdin.readline
loop = int(input())
room = []
for _ in range(loop):
    a, b = map(int, input().split())
    room.append((a,b))

room.sort(key=lambda x:(x[1], x[0]))

count = 1
end = room[0][1]
for i in range(1, len(room)):
    if room[i][0] >= end:
        count += 1
        end = room[i][1]
print(count)