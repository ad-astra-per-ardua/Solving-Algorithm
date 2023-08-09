import sys
input = sys.stdin.readline

MAX = 10

bitMask = [[-1 for _ in range(1 << MAX)] for _ in range(MAX)]
board = [['' for _ in range(MAX)] for _ in range(MAX)]


def dfs(lines, dfs_array, index, m):
    if m == index:
        line = ''.join(map(str, dfs_array))
        lines.append(line)
        return

    dfs_array[index] = 0
    dfs(lines, dfs_array, index + 1, m)

    if index > 0 and dfs_array[index - 1] != 0:
        return

    dfs_array[index] = 1
    dfs(lines, dfs_array, index + 1, m)


def dp(lines, line_number, before_bits, n, m):
    if n == line_number:
        return 0

    if bitMask[line_number][before_bits] > -1:
        return bitMask[line_number][before_bits]

    answer = 0
    for line in lines:
        bits = 0
        count = 0

        for i in range(m):
            if line[i] == '0':
                continue
            if board[line_number][i] == 'x':
                continue
            if i > 0 and (before_bits & (1 << (i - 1))):
                continue
            if i < m and (before_bits & (1 << (i + 1))):
                continue

            count += 1
            bits |= (1 << i)

        answer = max(answer, dp(lines, line_number + 1, bits, n, m) + count)

    bitMask[line_number][before_bits] = answer
    return answer


def solve():
    global bitMask, board
    for i in range(MAX):
        for j in range(1 << MAX):
            bitMask[i][j] = -1
    for i in range(MAX):
        for j in range(MAX):
            board[i][j] = 0

    n, m = map(int, input().split())

    for i in range(n):
        row = input().strip()
        for j in range(m):
            board[i][j] = row[j]

    dfs_array = [0] * MAX
    lines = []
    dfs(lines, dfs_array, 0, m)

    print(dp(lines, 0, 0, n, m))


if __name__ == "__main__":
    test_case = int(input())
    for _ in range(test_case):
        solve()
