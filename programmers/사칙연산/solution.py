// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/1843?language=python3

def solution(arr):
    n = (len(arr) + 1) // 2
    INF = float('inf')
    dp_max = [[-INF]*n for _ in range(n)]
    dp_min = [[INF]*n for _ in range(n)]
    nums = [int(arr[i]) for i in range(0, len(arr), 2)]
    ops = [arr[i] for i in range(1, len(arr), 2)]

    for i in range(n):
        dp_max[i][i] = nums[i]
        dp_min[i][i] = nums[i]

    for cnt in range(1, n):
        for i in range(n-cnt):
            j = i + cnt
            for k in range(i, j):
                if ops[k] == '+':
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] + dp_max[k+1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] + dp_min[k+1][j])
                else:
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] - dp_min[k+1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] - dp_max[k+1][j])

    return dp_max[0][n-1]
