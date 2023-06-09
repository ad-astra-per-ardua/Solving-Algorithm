from collections import deque

def bfs(n):
    q = deque([n])
    visited[n][0] = 0
    visited[n][1] = 1 
    
    while q:
        x = q.popleft()
        
        for i in [x - 1, x + 1, x * 2]:
            if 0 <= i <= 100000:
                if visited[i][0] == -1: # 처음 도달한다면
                    visited[i][0] = visited[x][0] + 1 # 걸린 시간 저장
                    visited[i][1] = visited[x][1] # 경우의 수 저장
                    q.append(i)
                    
                elif visited[i][0] == visited[x][0] + 1: # 처음이 아니라면 (하지만 최단 시간이라면)
                    visited[i][1] += visited[x][1] # 경우의 수 갱신
                    
n, k = map(int, input().split())
visited = [[-1, 0] for _ in range(100001)] # [지점 i에 도달하는데 걸린 시간, 경우의 수]

bfs(n)
print(visited[k][0])
print(visited[k][1])