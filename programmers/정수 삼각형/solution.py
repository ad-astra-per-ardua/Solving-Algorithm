// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/43105?language=python3

def solution(triangle):
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    return triangle[0][0]
