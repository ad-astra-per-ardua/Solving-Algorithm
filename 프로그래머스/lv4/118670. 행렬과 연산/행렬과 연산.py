from collections import deque

def solution(r, o):
    N = len(r)
    M = len(r[0])
    l = deque([r[i][0] for i in range(N)])
    m = deque([deque(r[i][1:M - 1]) for i in range(N)])
    rt = deque([r[i][M - 1] for i in range(N)])

    for op in o:
        if op == 'ShiftRow':
            l.appendleft(l.pop())
            m.appendleft(m.pop())
            rt.appendleft(rt.pop())
        else:
            m[0].appendleft(l.popleft())
            rt.appendleft(m[0].pop())
            m[N - 1].append(rt.pop())
            l.append(m[N - 1].popleft())
    a = []
    for i in range(N):
        a.append([l[i]] + list(m[i]) + [rt[i]])
    return a
