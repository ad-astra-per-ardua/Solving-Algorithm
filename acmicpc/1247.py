import sys
for _ in range(3):  # 3개의 테스트 케이스를 반복합니다.
    n = int(int(sys.stdin.readline().strip()))
    a = 0
    for i in range(n):
        s = int(int(sys.stdin.readline().strip()))
        a += s
    if a > 0:
        print('+')
    elif a == 0:
        print('0')
    else:
        print('-')
