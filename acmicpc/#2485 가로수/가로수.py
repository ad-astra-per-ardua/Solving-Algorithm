import math,sys
input = sys.stdin.readline

def gcd(a, b):
    while(b != 0):
        a, b = b, a % b
    return a

N = int(input())
trees = [int(input()) for _ in range(N)]
trees.sort()

gaps = [trees[i+1] - trees[i] for i in range(N-1)]
GCD = gaps[0]
for i in range(1, N-1):
    GCD = math.gcd(GCD, gaps[i])

answer = 0
for gap in gaps:
    answer += (gap // GCD) - 1

print(answer)
