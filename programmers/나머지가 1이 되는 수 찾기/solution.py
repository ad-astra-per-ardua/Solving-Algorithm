// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    answer = 0
    temp = []
    for i in range(1, n):
        if n % i == 1:
            temp.append(i)
    answer = min(temp)
            
            
    return answer