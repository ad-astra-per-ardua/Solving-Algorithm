def solution(n):
    base = "수"
    odd = "박수"
    even = "수박"
    if n % 2 == 0:
        return even*(n//2)
    else:
        return base + odd * ((n-1)//2)