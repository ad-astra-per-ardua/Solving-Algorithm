import sys
input = sys.stdin.readline
n, L = map(int, input().split())
leaks = list(map(int, input().split()))
leaks.sort()

tape = 1
end = leaks[0] + (L - 0.5)
for i in range(1, n):
    if leaks[i] <= end:
        continue
    else:
        tape += 1
        end = leaks[i] + (L - 0.5)

print(tape)
