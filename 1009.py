def answer_code(a, b):
    if b == 0:
        return 1
    if a % 10 == 0 or b % 10 == 0:
        return 10

    if a % 10 in (1, 5, 6):
        return a % 10
    elif a % 10 in (4, 9):
        cycle = 2
    else:
        cycle = 4

    b %= cycle
    if b == 0:
        b = cycle

    return (a ** b) % 10

loop = int(input())
for i in range(loop):
    a, b = map(int, input().split())
    print(answer_code(a, b))
