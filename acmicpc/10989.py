import sys

a = int(sys.stdin.readline())
counting = [0] * 10001

for _ in range(a):
    num = int(sys.stdin.readline())
    counting[num] += 1

for i in range(10001):
    if counting[i] != 0:
        for _ in range(counting[i]):
            print(i)
# AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA