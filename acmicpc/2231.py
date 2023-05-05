import sys
a = int(sys.stdin.readline())
result = 0

for i in range(1, a):
    decomposition_sum = i + sum(map(int, str(i)))
    if decomposition_sum == a:
        result = i
        break

print(result)
