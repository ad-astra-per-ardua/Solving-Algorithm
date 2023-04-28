import math

sign = [0] * 40558
sign[1] = 1

def sign_precompute():
    global sign
    for i in range(1, 40558):
        for j in range(2 * i, 40558, i):
            sign[j] -= sign[i]

def Q(x):
    global sign
    ans = 0
    for i in range(1, int(math.sqrt(x)) + 1):
        ans += sign[i] * (x // (i * i))
    return ans

if __name__ == "__main__":
    sign_precompute()
    k = int(input().strip())
    s, e, ans = 1, 1644934081, 1644934081
    while s <= e:
        m = s + (e - s) // 2
        if Q(m) < k:
            s = m + 1
        else:
            e = m - 1
            ans = m
    print(ans)
