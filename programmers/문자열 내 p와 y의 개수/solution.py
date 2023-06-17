// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    answer = False
    lists = s.lower()
    ans1 = []
    ans2 = []
    for i in range(len(lists)):
        if lists[i] == 'p':
            ans1.append(i)
        if lists[i] == 'y':
            ans2.append(i)
    if len(ans1) == len(ans2):
        answer = True
    else:
        answer = False
    return answer