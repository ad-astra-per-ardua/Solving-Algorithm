def solution(arr):
    temp = min(arr)
    return [-1] if len(arr) == 1 else [x for x in arr if x != temp]