def blank(n: int, array: list[int]) -> int:
    maximum = 0
    current = 0
    for i in range(n):
        if array[i] == 0:
            current += 1
            maximum = max(maximum, current)
        else:
            current = 0
    return maximum


t = int(input())
for i in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    result = blank(n, array)
    print(result)