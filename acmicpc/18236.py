def matrix_chain_order(matrices):
    n = len(matrices)
    m = [[0 if i == j else float('inf') for j in range(n)] for i in range(n)]

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + matrices[i][0] * matrices[k][1] * matrices[j][1]
                if q < m[i][j]:
                    m[i][j] = q

    return m[0][n - 1]

N = int(input())
matrices = [list(map(int, input().split())) for _ in range(N)]

print(matrix_chain_order(matrices))
