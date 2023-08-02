import sys
sys.setrecursionlimit(10000000)

MOD = 10**7 + 19
comb_list = [[0]*301 for _ in range(301)]

def combination(n, r) :
    if n == 1 or n == r or r == 0 :
        return 1
    if comb_list[n][r] :
        return comb_list[n][r]
    
    comb_list[n][r] = (combination(n-1, r-1) % MOD + combination(n-1, r) % MOD) % MOD
    return comb_list[n][r]
        

def count_1s(a, col, row) :
    result = [0] * row
    for i in range(col) :
        for j in range(row) :
            result[j] += a[i][j]
    
    return result

def make_dp(col, row, lst) :
    dp = [[0]*(col+1) for _ in range(row)]
    dp[0][col - lst[0]] = combination(col, lst[0])
    
    for i in range(1, row) :
        for j in range(col+1) :
            if dp[i-1][j] :
                tot_num = lst[i]
                for k in range(min(tot_num, j)+1) :
                    if col - j < tot_num - k :
                        continue
                    even = j + tot_num - 2*k
                    dp[i][even] += ( dp[i-1][j] % MOD * combination(j, k) % MOD * combination(col-j, tot_num - k) % MOD ) % MOD
    
    return dp

def solution(a):
    col, row = len(a), len(a[0])
    one_list = count_1s(a, col, row)
    dp = make_dp(col, row, one_list)

    return dp[-1][-1]
