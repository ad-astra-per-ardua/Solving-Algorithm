def process_test_case(n, t, durations, entertainment_values):
    max_entertainment = -1
    video_index = -1
    time_passed = 0
 
    for i in range(n):
        remaining_time = t - time_passed - durations[i]
        if remaining_time >= 0 and entertainment_values[i] > max_entertainment:
            max_entertainment = entertainment_values[i]
            video_index = i
        time_passed += 1
 
    return video_index + 1 if video_index != -1 else -1
 
q = int(input())
for _ in range(q):
    n, t = map(int, input().split())
    durations = list(map(int, input().split()))
    entertainment_values = list(map(int, input().split()))
    result = process_test_case(n, t, durations, entertainment_values)
    print(result)
