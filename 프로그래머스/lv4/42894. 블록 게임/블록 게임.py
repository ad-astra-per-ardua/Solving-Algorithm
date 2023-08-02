def canFill(row, col):
    for i in range(row):
        if Board[i][col]:
            return False
    return True

def find(row, col, h, w):
    emptyCnt = 0
    lastValue = -1

    for r in range(row, row+h):
        for c in range(col, col+w):
            if Board[r][c] == 0:
                if canFill(r, c) == False:
                    return False
                emptyCnt += 1

                if emptyCnt > 2:
                    return False
            else:
                if lastValue == -1:
                    lastValue = Board[r][c]
                elif lastValue != Board[r][c]:
                    return False
    for r in range(row, row+h):
        for c in range(col, col+w):
            Board[r][c] = 0
    return True

Board = []
def solution(board):
    global Board
    Board = board
    n = len(board)
    answer = 0
    while True:
        cnt = 0
        for i in range(n):
            for j in range(n):
                if i <= n-2 and j <= n-3 and find(i, j, 2, 3):
                    cnt += 1
                elif i <= n-3 and j <= n-2 and find(i, j, 3, 2):
                    cnt += 1
        answer += cnt
        if cnt == 0:
            break
    return answer