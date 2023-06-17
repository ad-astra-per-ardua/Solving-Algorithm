// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer