from collections import deque

d = [[-1,0],[0,1],[1,0],[0,-1]]

def spin(block):
	spin_block = [[0]*len(block) for _ in range(len(block[0]))]
	for row in range(len(block)):
		for col in range(len(block[0])):
			spin_block[col][len(spin_block[0])-1-row] = block[row][col]
	return spin_block

def catch_piece(table,row,col):
	R,C = len(table),len(table)
	piece = [[0]*C for _ in range(R)]
	piece[row][col] = 1
	q = deque([[row,col]])
	while q:
		r,c = q.popleft()
		piece[r][c] = 1
		table[r][c] = 0
		for i in d:
			dr,dc = i
			if 0 <= r+dr < R and 0 <= c+dc < C:
				if table[r+dr][c+dc] == 1:
					table[r+dr][c+dc] = 0
					piece[r+dr][c+dc] = 1
					q.append([r+dr,c+dc])

	r_piece = []
	for i in piece:
		if sum(i) != 0:
			r_piece.append(i)

	r_piece = spin(r_piece)
	c_piece = []
	for i in r_piece:
		if sum(i) != 0:
			c_piece.append(i)
	for _ in range(3):
		c_piece = spin(c_piece)

	return c_piece

def compare(game_board,piece,row,col):
	R,C = len(game_board),len(game_board)
	cnt = 0
	for r in range(len(piece)):
		for c in range(len(piece[0])):
			if piece[r][c] == 1 and game_board[row+r][col+c] == 2:
				cnt += 1
			elif piece[r][c] == 0 and game_board[row+r][col+c] == 1:
				continue
			else:
				return 0
	return cnt


def solution(game_board,table):
	answer = 0
	piece = deque()
	R,C = len(game_board),len(game_board)
	for row in range(R):
		for col in range(C):
			if table[row][col] == 1:
				piece.append(catch_piece(table,row,col))

	for row in range(R):
		for col in range(C):
			if game_board[row][col] == 0:
				q = deque([[row,col]])
				min_row,max_row = row,row
				min_col,max_col = col,col
				while q:
					r,c = q.popleft()
					game_board[r][c] = 2
					for i in d:
						dr,dc = i
						if 0 <= r+dr < R and 0 <= c+dc < C:
							if game_board[r+dr][c+dc] == 0:
								q.append([r+dr,c+dc])
								min_row,max_row = min(min_row,r+dr),max(max_row,r+dr)
								min_col,max_col = min(min_col,c+dc),max(max_col,c+dc)
								game_board[r+dr][c+dc] = 2

				result = 0
				for p in range(len(piece)):
					for _ in range(4):
						if piece[p][0][0] == -1:
							break
						if len(piece[p]) == max_row-min_row+1 and len(piece[p][0]) == max_col-min_col+1:
							result = compare(game_board,piece[p],min_row,min_col)

							if result > 0:
								answer += result
								piece[p][0][0] = -1
								break
						piece[p] = spin(piece[p])
					if result > 0:
						break

	return answer