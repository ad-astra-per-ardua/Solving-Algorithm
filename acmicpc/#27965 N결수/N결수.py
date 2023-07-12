import sys
input = sys.stdin.readline

N, K = map(int, input().split())
result = 0
ten = 1

for i in range(1, N + 1):
    while i >= ten:
        ten *= 10
    result = (result * ten + i) % K

print(result)
