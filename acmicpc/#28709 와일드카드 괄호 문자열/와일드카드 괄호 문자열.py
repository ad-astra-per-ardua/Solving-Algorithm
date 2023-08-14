import sys
input = sys.stdin.readline

def solve(s):
    s = list(s)
    if s.count('*') >= 1:
        count = 0
        for c in s:
            if c == "*":
                break
            if c == ')':
                count -= 1
            else:
                 count += 1
            if count < 0:
                return False
        count = 0
        for c in s[::-1]:
            if c=='*':
                break
            if c=='(':
                count-=1
            else:
                count+=1
            if count<0:
                return False
        return True
    if len(s)%2!=0:
        return False
    op = s.count('(')
    cl=s.count(')')
    if op>len(s)//2 or cl>len(s)//2:
        return False
    count = 0
    for c in s:
        if c =='?':
            if op<len(s)//2:
                c='('
                op+=1
            else:
                c=")"
        if c=='(':
            count +=1
        else:
            count-=1
        if count<0:
            return False
    return True

t = int(input())
for _ in range(t):
    s = input().rstrip()
    if solve(s) == True:
        print("YES")
    else:
        print("NO")
