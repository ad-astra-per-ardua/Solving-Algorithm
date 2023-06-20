// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/150369

def solution(cap, n, deliveries, pickups):
    answer = 0
    dv = [[i+1, deliveries[i]] for i in range(n) if deliveries[i] != 0]
    pu = [[i+1, pickups[i]] for i in range(n) if pickups[i] != 0]

    def solve(stack):
        if not stack:
            return 0
        distance = 0
        capacity = cap
        while capacity > 0 and stack:
            loca, amount = stack[-1]
            if amount <= capacity:
                distance = max(distance, loca)
                capacity -= stack.pop()[1]
            else:
                stack[-1][1] -= capacity
                distance = max(distance, loca)
                capacity = 0
        return distance

    def final():
        return max(solve(dv), solve(pu))

    while dv or pu:
        answer += final()

    return answer * 2
