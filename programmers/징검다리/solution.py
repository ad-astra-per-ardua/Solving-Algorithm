// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/43236?language=python3

def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    
    left, right = 0, distance
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        prev = 0
        remove_cnt = 0
        min_distance = float('inf')

        for rock in rocks:
            if rock - prev < mid:
                remove_cnt += 1
            else:
                min_distance = min(min_distance, rock - prev)
                prev = rock
        
        if remove_cnt > n:
            right = mid - 1
        else:
            answer = min_distance
            left = mid + 1
    
    return answer
