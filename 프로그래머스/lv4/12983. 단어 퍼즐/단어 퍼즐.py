def solution(strs, t):
    INF = int(10e+8)
    d = [INF] * len(t) + [0]
    for i in range(len(t)-1, -1, -1):
        for j in range(1, min(6, len(t)-i+1)):
            if t[i:i+j] in strs:
                d[i] = min(d[i], d[i+j]+1)
    return -1 if d[0]==INF else d[0]