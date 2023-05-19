n = int(input())
m = n
attempt = 0
in_sum = 0
end = 0
for start in range(1, n+1):
    while in_sum < m and end < n:
        end += 1
        in_sum += end
    if in_sum == m:
        attempt += 1
    in_sum -= start
print(attempt)