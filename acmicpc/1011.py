import math

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    distance = y - x
    max_move = math.floor(math.sqrt(distance))

    if distance == max_move ** 2:
        print(max_move * 2 - 1)
    elif max_move ** 2 < distance <= max_move ** 2 + max_move:
        print(max_move * 2)
    else:
        print(max_move * 2 + 1)
