from collections import defaultdict
import sys

def dfs(sales, idx, dp, link):
    dp[idx][0] = 0
    dp[idx][1] = sales[idx - 1]
    
    if len(link[idx]) == 0: return
    extra = sys.maxsize
    for child in link[idx]:
        dfs(sales, child, dp, link)
        if dp[child][0] < dp[child][1]:
            dp[idx][0] += dp[child][0]
            dp[idx][1] += dp[child][0]
            extra = min(extra, dp[child][1] - dp[child][0])
        else:
            dp[idx][0] += dp[child][1]
            dp[idx][1] += dp[child][1]
            extra = 0
    
    dp[idx][0] += extra


def solution(sales, links):
    link = defaultdict(list)
    
    for a, b in links:
        link[a].append(b)
    
    dp = [[0, 0] for _ in range(len(sales) + 1)]
    
    dfs(sales, 1, dp, link)
    answer = min(dp[1][0], dp[1][1])
    return answer