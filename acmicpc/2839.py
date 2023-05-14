a = int(input())
stack = 0
while True:
    if a % 5 == 0:
        stack += a // 5
        print(stack)
        break
    elif a<= 0:
        print(-1)
        break
    a -= 3
    stack += 1
