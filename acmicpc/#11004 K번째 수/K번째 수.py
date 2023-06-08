import sys,itertools
input = sys.stdin.readline

n, k = map(int,input().split())

lists = list(map(int,input().split()))
lists.sort()
print(lists[k-1])