import sys
from sys import stdin, setrecursionlimit
from types import GeneratorType

def ceil(x): return int(x) if(x == int(x)) else int(x)+1
def ceildiv(x, d): return x//d if(x % d == 0) else x//d+1

MOD = 1_000_000_007
# setrecursionlimit(10**6)
input = lambda: stdin.readline().strip()

######### main code goes here #########

def solve():
    t = int(input())
    ans = []

    moves = [
        (1, 2), (1, -2), (-1, 2), (-1, -2),
        (2, 1), (2, -1), (-2, 1), (-2, -1)
    ]

    def temp(x, y):
        x, y = abs(x), abs(y)
        if x > y:
            x, y = y, x

        if x == 0 and y == 1: return 3
        if x == 2 and y == 2: return 4

        dist = max((y + 1) // 2, (x + y + 2) // 3)
        if (dist % 2) != ((x + y) % 2):
            dist += 1

        return dist

    for _ in range(t):
        tx,ty = map(int, input().split())
        move1 = temp(tx, ty)

        if move1 <= 1:
            ans.append("-1")
            continue

        count = 0
        for a, b in moves:
            remain = temp(tx - a, ty - b)
            if remain + 1 == move1:
                count += 1

        ans.append(str(count))

    sys.stdout.write('\n'.join(ans) + '\n')


if __name__ == '__main__':
    solve()
