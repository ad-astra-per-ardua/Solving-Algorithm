from itertools import permutations
import sys,math
input = sys.stdin.readline
n = int(input())
lists = []
for e in range(1,n+1):
    lists.append(e)

ans_list = list(permutations(lists,n))
for i in range(math.factorial(n)):
    print(*ans_list[i])