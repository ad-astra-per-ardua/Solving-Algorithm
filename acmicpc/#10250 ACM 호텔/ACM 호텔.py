import sys
input = sys.stdin.readline
loop = int(input())

for _ in range(loop):
    floor, rooms, person = map(int, input().split())
    hotel = [[0]* rooms for _ in range(floor)]
    for e in range(rooms):
        for i in range(floor):
            hotel[i][e] = 'a'
            person -= 1
            if person == 0:
                if e >= 9:
                    print(f"{i+1}{e+1}")
                else:
                    print(f"{i + 1}0{e + 1}")