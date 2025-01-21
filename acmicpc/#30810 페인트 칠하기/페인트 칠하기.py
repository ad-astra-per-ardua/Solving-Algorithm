import sys
sys.setrecursionlimit(10**7)

input=sys.stdin.readline

def main():
    N, M, K = map(int, input().split())
    R = list(map(int, input().split())) 
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v, c = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append((v,c))
        G[v].append((u,c))

    vis = [0]*N
    history = []

    def dfs(u):
        vis[u] += 1
        history.append(u)
        if vis[u] == 1:
            for (v,c) in G[u]:
                if R[u] == c:  
                    if vis[v] != 2:
                        ret = dfs(v)
                        history.append(u)
                        return ret
                    else:
                        history.append(v)
                        return dfs(u)
            return False
        else:
            for (v,c) in G[u]:
                if vis[v] != 2:
                    if not dfs(v):
                        return False
                    history.append(u)
            return True

    res = dfs(0)
    if (not res) or any(x != 2 for x in vis):
        print("NO")
    else:
        print("YES")
        print(len(history))
        history.reverse()
        print(*[h+1 for h in history])

if __name__=="__main__":
    main()
