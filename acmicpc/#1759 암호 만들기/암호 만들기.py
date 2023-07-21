from itertools import combinations
import sys
input = sys.stdin.readline

def solve():
    result = []
    for i in list(combinations(chars, l)):
        v_count = c_count = 0
        for char in i:
            if char in v:
                v_count += 1
            else:
                c_count += 1
        if v_count > 0 and c_count > 1:
            result.append("".join(i))
    return result


l, c = map(int, input().split())
chars = sorted(input().split())
v = {'a', 'e', 'i', 'o', 'u'}
for r in solve():
    print(r)
