def solve():
    K = int(input().strip())
    S = input().strip()

    answer, count_N, count_S = 0, [0]*(K+1), [0]*(K+1)
    for i in range(1, K+1):
        if S[i-1] == 'N':
            count_N[i] = count_N[i-1] + 1
            count_S[i] = count_S[i-1]
        else:
            count_N[i] = count_N[i-1]
            count_S[i] = count_S[i-1] + 1

    start, end = 0, 0
    while end <= K:
        if count_N[end] == count_S[end]:
            half = (end - start) // 2
            if S[start] != S[start+half]:
                answer = max(answer, end - start)
            start = end
        end += 1

    print(answer)

solve()
