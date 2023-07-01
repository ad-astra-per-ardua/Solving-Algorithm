// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/43164?language=python3

def solution(tickets):
    routes = dict()
    for start, end in tickets:
        if start in routes:
            routes[start].append(end)
        else:
            routes[start] = [end]
    for start in routes:
        routes[start].sort(reverse=True)
    stack = ["ICN"]
    path = []
    while stack:
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top].pop())
    return path[::-1]
