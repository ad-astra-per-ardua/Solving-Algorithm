import sys
from bisect import bisect_left

def calculate(tree1, tree2):
    left_sum, left_l_sum, left_r_sum, left_max = tree1
    right_sum, right_l_sum, right_r_sum, right_max = tree2

    total_sum = left_sum + right_sum
    l_sum = max(left_l_sum, left_sum + right_l_sum)
    r_sum = max(right_r_sum, right_sum + left_r_sum)
    max_sum = max(left_max, right_max, left_r_sum + right_l_sum)

    return (total_sum, l_sum, r_sum, max_sum)

def update(seg_tree, idx, weight):
    idx += SEG_MAX // 2
    seg_tree[idx] = (
        seg_tree[idx][0] + weight,
        seg_tree[idx][1] + weight,
        seg_tree[idx][2] + weight,
        seg_tree[idx][3] + weight,
    )

    while idx > 1:
        idx //= 2
        seg_tree[idx] = calculate(seg_tree[idx * 2], seg_tree[idx * 2 + 1])

def main():
    input = sys.stdin.read
    data = input().split()

    idx = 0
    num_strike = int(data[idx])
    idx += 1

    strikes = []
    strike_x_pos = []
    strike_y_pos = []

    for _ in range(num_strike):
        x, y = int(data[idx]), int(data[idx + 1])
        strikes.append((x, y))
        strike_x_pos.append(x)
        strike_y_pos.append(y)
        idx += 2

    num_ball = int(data[idx])
    idx += 1

    balls = []
    ball_x_pos = []
    ball_y_pos = []

    for _ in range(num_ball):
        x, y = int(data[idx]), int(data[idx + 1])
        balls.append((x, y))
        ball_x_pos.append(x)
        ball_y_pos.append(y)
        idx += 2

    c1, c2 = int(data[idx]), int(data[idx + 1])

    total_points = []
    x_pos = []
    y_pos = []

    for x, y in strikes:
        total_points.append((x, y, c1))
        x_pos.append(x)
        y_pos.append(y)

    for x, y in balls:
        total_points.append((x, y, -c2))
        x_pos.append(x)
        y_pos.append(y)

    x_pos = sorted(set(x_pos))
    y_pos = sorted(set(y_pos))

    cache = [[] for _ in range(len(y_pos))]

    for x, y, w in total_points:
        x_idx = bisect_left(x_pos, x)
        y_idx = bisect_left(y_pos, y)
        cache[y_idx].append((x_idx, w))

    global SEG_MAX
    SEG_MAX = 1 << (len(x_pos).bit_length() + 1)
    seg_tree = [(0, 0, 0, 0) for _ in range(2 * SEG_MAX)]

    max_eval = 0

    for y1 in range(len(y_pos)):
        seg_tree = [(0, 0, 0, 0) for _ in range(2 * SEG_MAX)]
        for y2 in range(y1, len(y_pos)):
            for x_idx, w in cache[y2]:
                update(seg_tree, x_idx, w)

            max_eval = max(max_eval, seg_tree[1][3])

    print(max_eval)

if __name__ == "__main__":
    main()
