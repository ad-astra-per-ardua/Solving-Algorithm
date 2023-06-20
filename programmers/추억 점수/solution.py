// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/176963

def solution(name, yearning, photo):
    answer = []
    name_yearning_dict = dict(zip(name, yearning))

    for pic in photo:
        total_score = 0
        for person in pic:
            if person in name_yearning_dict:
                total_score += name_yearning_dict[person]
        answer.append(total_score)
    return answer