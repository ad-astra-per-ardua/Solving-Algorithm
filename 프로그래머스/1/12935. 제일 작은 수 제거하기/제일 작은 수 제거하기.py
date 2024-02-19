def solution(arr):
    temp = min(arr)
    if len(arr) == 1:
        return [-1]
    answer = [x for x in arr if x is not temp]
    return answer