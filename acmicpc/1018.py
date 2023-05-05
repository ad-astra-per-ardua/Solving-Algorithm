def min_squares_to_repaint(N, M, board):
    min_repaints = float('inf')

    for start_row in range(N - 7):
        for start_col in range(M - 7):
            repaints1 = 0
            repaints2 = 0
            for row in range(start_row, start_row + 8):
                for col in range(start_col, start_col + 8):
                    if (row + col) % 2 == 0:
                        if board[row][col] == 'B':
                            repaints1 += 1
                        else:
                            repaints2 += 1
                    else:
                        if board[row][col] == 'W':
                            repaints1 += 1
                        else:
                            repaints2 += 1
            min_repaints = min(min_repaints, repaints1, repaints2)

    return min_repaints
N, M = map(int,(input().split()))
board = [input() for _ in range(N)]

result = min_squares_to_repaint(N, M, board)
print(result)
