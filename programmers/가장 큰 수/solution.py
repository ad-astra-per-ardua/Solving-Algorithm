// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3)
    numbers.reverse()
    answer =  str(int(''.join(numbers)))
    return answer