import sys
input = sys.stdin.readline
n = int(input())
maze = list(map(int, input().split()))
jumps = [0] + [float('inf')] * (n-1) 

for i in range(n):
    if jumps[i] == float('inf'): 
        continue
    for j in range(1, maze[i]+1): 
        if i + j < n: 
            jumps[i+j] = min(jumps[i+j], jumps[i] + 1)

print(jumps[-1] if jumps[-1] != float('inf') else -1) 
