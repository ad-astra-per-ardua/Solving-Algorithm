import sys

while True:
    # 사탕 종류 n, 돈의 양 m
    n, m = map(float, sys.stdin.readline().split())

    n = int(n)
    m = int(m * 100 + 0.5)

    # 종료조건
    if n == 0 and m == 0:
        break

    c = []  # 칼로리
    p = []  # 가격
    for i in range(n):
        calorie, price = map(float, sys.stdin.readline().split())
        c.append(int(calorie))
        p.append(int(price * 100 + 0.5))

    # 돈 m은 계산하기 용이하도록 x100 (0.01~ -> 1~)
    dp = [0 for i in range(m + 1)]
    max_c_per_p = [0 for _ in range(m + 1)]  # 가격 별 칼로리 최댓값

    for i in range(n):
        for j in range(p[i], m + 1):
            max_c_per_p[j] = max(max_c_per_p[j], max_c_per_p[j - p[i]] + c[i])

    for i in range(1, m + 1):
        dp[i] = max(max_c_per_p[i], dp[i - 1])

    print(dp[m])
