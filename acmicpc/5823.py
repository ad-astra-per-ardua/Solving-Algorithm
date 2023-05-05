import math

def init(N, L, X):
    global positions, cameras, bucket_size, buckets
    positions = X[:]
    cameras = L
    bucket_size = int(math.sqrt(N))
    buckets = [sorted(positions[i:i + bucket_size]) for i in range(0, N, bucket_size)]

def update(i, y):
    global positions, cameras, bucket_size, buckets
    old_position = positions[i]
    positions[i] = y

    for b in buckets:
        if old_position in b:
            b.remove(old_position)
            break

    for b in buckets:
        if len(b) == 0 or (b[-1] >= y and b[0] <= y):
            b.append(y)
            b.sort()
            break
    else:
        new_bucket = [y]
        buckets.append(new_bucket)

    if len(buckets[-1]) > 2 * bucket_size:
        mid = len(buckets[-1]) // 2
        new_bucket = buckets[-1][mid:]
        buckets[-1] = buckets[-1][:mid]
        buckets.append(new_bucket)

    min_cameras = 0
    for b in buckets:
        min_cameras += count_cameras(b, cameras)

    return min_cameras

def count_cameras(bucket, L):
    if not bucket:
        return 0

    count = 1
    last_camera_position = bucket[0] + L
    for position in bucket[1:]:
        if position > last_camera_position:
            count += 1
            last_camera_position = position + L
        elif position == last_camera_position:
            last_camera_position = position + L

    return count

N, L, M = map(int, input().split())
X = [int(input()) for _ in range(N)]
init(N, L, X)

for _ in range(M):
    i, y = map(int, input().split())
    print(update(i, y))
