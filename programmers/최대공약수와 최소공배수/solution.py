// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/12940

import math
def solution(n, m):
    def lcm(a, b):
        return (a * b) // math.gcd(a, b)
    ans1 = math.gcd(n,m)
    ans2 = lcm(n,m)
    answer = [ans1,ans2]
    return answer