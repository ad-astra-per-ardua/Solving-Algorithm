def cal_time(heights, target_height, blocks):
    remove_time = 0
    add_time = 0
    for height in heights:
        if height > target_height:
            remove_time += height - target_height
        elif height < target_height:
            add_time += target_height - height
    return (remove_time * 2 + add_time, blocks + remove_time >= add_time)

N, M, B = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(N)]

heights = []
for row in land:
    heights.extend(row)

min_time = float('inf')
result_height = 0

for target_height in range(257):
    time, can_build = cal_time(heights, target_height, B)
    if can_build and time <= min_time:
        min_time = time
        result_height = target_height

print(min_time, result_height)
