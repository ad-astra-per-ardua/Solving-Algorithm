input_lines = []
for _ in range(4):
    input_lines.append(input().strip())

depth = 0
for line in input_lines:
    direction, steps = line.split()
    steps = int(steps)

    if direction == "Es":
        depth += 21 * steps
    elif direction == "Stair":
        depth += 17 * steps

print(depth)