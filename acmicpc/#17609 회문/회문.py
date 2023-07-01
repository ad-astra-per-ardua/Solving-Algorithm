import sys
input = sys.stdin.readline

string = []
t = int(input())
for _ in range(t):
    string.append(input().rstrip())


def is_palindrome(start, end, temp):
    while start <= end:
        if i[start] == i[end]:
            start += 1
            end -= 1
        else:
            if temp == 0:
                left = is_palindrome(start + 1, end, temp + 1)
                right = is_palindrome(start, end - 1, temp + 1)
                return min(left, right)
            else:
                return 2
    return temp


answer = []
for i in string:
    start, end = 0, len(i) - 1
    answer.append(is_palindrome(start, end, 0))

for r in answer:
    print(r)