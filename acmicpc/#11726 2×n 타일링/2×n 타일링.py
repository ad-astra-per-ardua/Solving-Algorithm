
mod = 10007
mem = [0] * 1001
mem[1] = 1
mem[2] = 2

def tiling(n):
    if mem[n] == 0:
        mem[n] = tiling(n-1) + tiling(n-2)
        mem[n] %= mod
    return mem[n]
n = int(input())
print(tiling(n))