import sys
input = sys.stdin.readline

n = input()
card1 = set(map(int, input().split()))
m = input()
card2 = list(map(int, input().split()))

for i in card2:
    if i in card1:
        print(1, end=' ')
    else:
        print(0, end=' ')