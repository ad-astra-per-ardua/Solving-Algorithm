import sys
input = sys.stdin.readline
n, m = map(int, input().split())
deck = list(map(int, input().split()))
deck.sort()
ans = []

for i in range(0,len(deck)-2):
    for e in range(1, len(deck)-1):
        for j in range(2, len(deck)):
            if deck[i] + deck[e] + deck[j] <= m and i < e < j:
                temp = deck[i] + deck[e] + deck[j]
                ans.append(temp)

ans.sort()
print(max(ans))