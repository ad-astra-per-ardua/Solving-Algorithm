// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/132267

def solution(a, b, n):
    answer = 0
    while n >= a:
        q, r = divmod(n,a)
        answer += q * b
        n = r + q * b
    return answer