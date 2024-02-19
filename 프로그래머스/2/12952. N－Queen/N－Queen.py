def solve1(row, col, ld, rd, n, count):
    if row == n:
        count[0] += 1
        return

    pos = ((1 << n) - 1) & (~(col | ld | rd))
    while pos:
        p = pos & -pos
        pos -= p
        solve1(row + 1, col | p, (ld | p) << 1, (rd | p) >> 1, n, count)

def solution(n):
    count = [0]
    solve1(0, 0, 0, 0, n, count)
    return count[0]
