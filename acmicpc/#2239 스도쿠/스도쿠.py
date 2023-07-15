import sys
input = sys.stdin.readline

def dfs(idx):
    if idx == len(empty):
        for i in range(9):
            print("".join(map(str,matrix[i])))
        return True
    i, j = empty[idx][0], empty[idx][1]
    total_number = set([num for num in range(1,10)])
    used = set(matrix[i] + [matrix[r][j] for r in range(9)] + [matrix[r][c] for r in range(3*(i//3),3*(i//3)+3) for c in range(3*(j//3), 3*(j//3) +3)])
    for num in sorted(total_number - used):
        matrix[i][j] = num
        if dfs(idx+1):
            return True
        matrix[i][j] = 0
    return False

matrix = [list(map(int,list(input().rstrip()))) for _ in range(9)]
empty = [(i,j) for i in range(9) for j in range(9) if not matrix[i][j]]
dfs(0)