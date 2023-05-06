def solve(n, m):
    if n == m:
        return True
    if n < m:
        return False
    if n % 3 == 0:
        return solve(n // 3, m) or solve((2 * n) // 3, m)
    return False


if __name__ == '__main__':
    for _ in range(int(input())):
        n, m = map(int, input().split())
        print('YES' if solve(n, m) else 'NO')