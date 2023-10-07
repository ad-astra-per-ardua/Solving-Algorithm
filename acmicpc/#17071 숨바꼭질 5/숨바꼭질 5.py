from collections import deque
import sys
input = sys.stdin.readline

def chk(loc):
    return 0 <= loc <= 500000

def main():
    N, K = map(int, input().split())

    visited = [[-1 for _ in range(500001)] for _ in range(2)]
    que = deque([(N, 0)])
    
    while que:
        subinLoc, subinTime = que.popleft()
        
        if not chk(subinLoc):
            continue
        if visited[subinTime % 2][subinLoc] != -1:
            continue
        
        visited[subinTime % 2][subinLoc] = subinTime
        
        que.append((subinLoc - 1, subinTime + 1))
        que.append((subinLoc + 1, subinTime + 1))
        que.append((subinLoc * 2, subinTime + 1))

    flag = False
    for i in range(500001):
        nextK = K + (i * (i + 1)) // 2
        if nextK > 500000:
            break
        if visited[i % 2][nextK] != -1 and visited[i % 2][nextK] <= i:
            print(i)
            flag = True
            break

    if not flag:
        print(-1)

if __name__ == "__main__":
    main()
