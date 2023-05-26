from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
numbers = sorted(set(numbers))

print(" ".join(map(str,numbers)))