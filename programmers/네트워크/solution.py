// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/43162?language=python3

def dfs(computers, visited, start):
    stack = [start]
    while stack:
        j = stack.pop()
        if visited[j] == 0:
            visited[j] = 1
        for i in range(len(computers)):
            if computers[j][i] == 1 and visited[i] == 0:
                stack.append(i)

def solution(n, computers):
    visited = [0 for _ in range(n)]
    answer = 0
    while 0 in visited:
        dfs(computers, visited, visited.index(0))
        answer += 1
    return answer
