from string import ascii_lowercase
import sys
input = sys.stdin.readline

standard = list(ascii_lowercase)
answer = []
s = list(input())

for i in standard:
    try:
        temp = s.index(i)
        answer.append(temp)
    except ValueError:
        answer.append(-1)
print(*answer)