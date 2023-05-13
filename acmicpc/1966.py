loop = int(input())
for _ in range(loop):
    a, b = map(int, input().split())
    test = list(map(int, input().split()))  # a = 문서 갯수, b = 현재 큐에서 좌표
    target = b
    cord = 0

    while True:
        if test[0] < max(test):
            if target == 0:
                target = len(test) - 1
            else:
                target -= 1
            test.append(test.pop(0))
        else:
            test.pop(0)
            cord += 1
            if target == 0:
                print(cord)
                break
            else:
                target -= 1