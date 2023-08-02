dy = (1, 0, -1, 0)
dx = (0, -1, 0, 1)
 
def solution(grid):
    answer = []
 
    ly, lx = len(grid), len(grid[0])
 
    visited = [[[False] * 4 for _ in range(lx)] for _ in range(ly)]
 
    for y in range(ly):
        for x in range(lx):
            for d in range(4):
                if visited[y][x][d]:
                    continue
                
                count = 0
                ny, nx = y, x
                while not visited[ny][nx][d]:
                    visited[ny][nx][d] = True
                    count += 1
                    if grid[ny][nx] == "S":
                        pass
                    elif grid[ny][nx] == "L":
                        d = (d - 1) % 4
                    elif grid[ny][nx] == "R": 
                        d = (d + 1) % 4
                    
                    ny = (ny + dy[d]) % ly 
                    nx = (nx + dx[d]) % lx
 
                answer.append(count)
    answer = sorted(answer) 
    return answer
