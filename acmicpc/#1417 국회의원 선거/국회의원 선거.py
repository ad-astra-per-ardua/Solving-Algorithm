import sys, heapq as hp
input = sys.stdin.readline

n = int(input())
win = int(input())
lists = []

for _ in range(n - 1):
    num = int(input())
    hp.heappush(lists, (-num, num))

count = 0
while lists:
    num = hp.heappop(lists)[1]
    if num >= win:
        num -= 1
        win += 1
        count += 1
        hp.heappush(lists, (-num, num))

print(count)