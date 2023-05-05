a = int(input())
for i in range(a):
    a, b, c = map(int,input().split())
    if a + b == c:
        print('+')
    elif a - b == c:
        print('-')
