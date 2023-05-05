a, b = map(int, input().split())
lan_sun = [int(input()) for _ in range(a)]

start, end = 1, max(lan_sun)

result = 0
while start <= end:
    mid = (start + end) // 2
    total_sundle = sum(lan // mid for lan in lan_sun)

    if total_sundle >= b:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
