a, b = map(int, input().split())

lists = [list(input().strip()) for _ in range(a)]
min_changes = float('inf')

for x in range(a - 7):
    for y in range(b - 7):
        for start_color in ('W', 'B'):
            count = 0
            for i in range(x, x + 8):
                for j in range(y, y + 8):
                    if (i + j) % 2 == 0:
                        if lists[i][j] != start_color:
                            count += 1
                    else:
                        if lists[i][j] == start_color:
                            count += 1
            min_changes = min(min_changes, count)

print(min_changes)
