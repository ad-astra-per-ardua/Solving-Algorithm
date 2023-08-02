dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

class Result:
    def __init__(self, win, move_cnt):
        self.win = win
        self.move_cnt = move_cnt

def is_move_possible(board, x, y, height, width):
    if x < 0 or x >= height or y < 0 or y >= width or board[x][y] == 0:
        return False
    return True

def dfs(board, ax, ay, bx, by, a_depth, b_depth, height, width):
    win = False
    win_cnt = height * width
    lose_cnt = a_depth + b_depth

    if a_depth == b_depth and board[ax][ay] == 1:
        for d in range(4):
            nx = ax + dx[d]
            ny = ay + dy[d]
            if not is_move_possible(board, nx, ny, height, width):
                continue
            board[ax][ay] = 0
            r = dfs(board, nx, ny, bx, by, a_depth+1, b_depth, height, width)
            win |= not r.win
            if r.win:
                lose_cnt = max(lose_cnt, r.move_cnt)
            else:
                win_cnt = min(win_cnt, r.move_cnt)
            board[ax][ay] = 1
    elif a_depth > b_depth and board[bx][by] == 1:
        for d in range(4):
            nx = bx + dx[d]
            ny = by + dy[d]
            if not is_move_possible(board, nx, ny, height, width):
                continue
            board[bx][by] = 0
            r = dfs(board, ax, ay, nx, ny, a_depth, b_depth+1, height, width)
            win |= not r.win
            if r.win:
                lose_cnt = max(lose_cnt, r.move_cnt)
            else:
                win_cnt = min(win_cnt, r.move_cnt)
            board[bx][by] = 1

    return Result(win, win_cnt if win else lose_cnt)

def solution(board, aloc, bloc):
    height = len(board)
    width = len(board[0])
    return dfs(board, aloc[0], aloc[1], bloc[0], bloc[1], 0, 0, height, width).move_cnt
