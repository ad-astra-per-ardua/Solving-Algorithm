import sys
sys.setrecursionlimit(10**9)
def matrix_chain_order(matrices):
    n = len(matrices)
    m = [0] * n

    def cost(i, k, j):
        return matrices[i][0] * matrices[k][1] * matrices[j][1]

    def hu_shing_algorithm(i, j):
        if i == j:
            return 0
        min_cost = float('inf')
        for k in range(i, j):
            q = hu_shing_algorithm(i, k) + hu_shing_algorithm(k + 1, j) + cost(i, k, j)
            if q < min_cost:
                min_cost = q
        return min_cost

    return hu_shing_algorithm(0, n - 1)

N = int(input())
matrices = [list(map(int, input().split())) for _ in range(N)]

print(matrix_chain_order(matrices))