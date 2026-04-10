from sys import stdin, setrecursionlimit

def ceil(x): return int(x) if(x == int(x)) else int(x)+1
def ceildiv(x, d): return x//d if(x % d == 0) else x//d+1

MOD = 1_000_000_007
# setrecursionlimit(10**6)
input = lambda: stdin.readline().strip()

######### main code goes here #########

def solve():
    n = int(input())
    d = list(map(int,input().split()))
    b, c = map(int, input().split())
    count = 0
    for i in range(n):
        d[i] -= b
        count += 1
        if d[i] > 0:
            count += ceildiv(d[i], c)
    print(count)


if __name__ == '__main__':
    solve()