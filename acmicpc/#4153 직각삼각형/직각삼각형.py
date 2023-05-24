while True:
    cases = list(map(int, input().split()))
    cases.sort()
    a, b, c = cases
    if a == 0 and b == 0 and c == 0:
        break
    if c ** 2 == (b ** 2 + a ** 2 ):
        print('right')
    else:
        print("wrong")