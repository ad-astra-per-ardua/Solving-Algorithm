import sys
input = sys.stdin.readline

n = int(input())
lists = list(map(int, input().split()))
lists.sort()
lists.pop()
print(sum(lists))