ss = input()
m = list(input())

stack = []
for i in range(len(ss)):
    stack.append(ss[i])
    if stack[-len(m):] == m:
        del stack[-len(m):]
if stack: print("".join(stack))
else: print("FRULA")