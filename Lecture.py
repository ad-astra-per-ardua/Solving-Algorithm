def make_spiral_matrix(N):
    matrix = [[0]*N for _ in range(N)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    num = 1
    x, y = 0, 0
    direction = 0

    while num <= N*N:
        matrix[x][y] = num
        num += 1

        nx, ny = x + dx[direction], y + dy[direction]

        if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] == 0:
            x, y = nx, ny
        else:
            direction = (direction + 1) % 4
            x, y = x + dx[direction], y + dy[direction]

    return matrix

N = int(input())
matrix = make_spiral_matrix(N)
row, col = map(int,input().split())

print(matrix[row-1][col-1])
