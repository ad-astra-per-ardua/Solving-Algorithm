import sys
input = sys.stdin.readline
N = int(input())
words = [input().strip() for _ in range(N)]
alpha = [0 for _ in range(26)]

for word in words:
    i = 0
    j = len(word) - 1
    while j >= 0:
        alpha[ord(word[i]) - ord('A')] += pow(10, j)
        j -= 1
        i += 1

alpha.sort(reverse=True)
answer = 0
for i in range(9, 0, -1):
    answer += i * alpha[9 - i]

print(answer)
