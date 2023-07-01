import sys
input = sys.stdin.readline
def recursion(s, l, r):
    global count
    count += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    global count
    count = 0
    return recursion(s, 0, len(s)-1)

loop = int(input().rstrip())
for _ in range(loop):
    print(isPalindrome(input().rstrip()),count)