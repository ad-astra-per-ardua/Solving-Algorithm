def matrix_chain_order(matrices):
    n = len(matrices)
    m = [[0] * n for _ in range(n)]

    def cost(i, j, k):
        return matrices[i][0] * matrices[k][1] * matrices[j][1]

    def hu_shing_algorithm(i, j):
        if m[i][j] > 0:
            return m[i][j]
        if i == j:
            m[i][j] = 0
        else:
            m[i][j] = float('inf')
            for k in range(i, j):
                q = hu_shing_algorithm(i, k) + hu_shing_algorithm(k + 1, j) + cost(i, k, j)
                if q < m[i][j]:
                    m[i][j] = q
        return m[i][j]

    return hu_shing_algorithm(0, n - 1)

N = int(input())
matrices = [list(map(int, input().split())) for _ in range(N)]

print(matrix_chain_order(matrices))