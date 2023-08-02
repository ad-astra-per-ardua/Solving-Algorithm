mod = 1000000007

def solution(n, count):
    arr = [[0] * (count + 1) for _ in range(n + 1)]
    arr[1][1] = 1

    for row in range(2, n + 1):
        prevRow = row - 1
        nextColLength = min(count, row)

        for col in range(1, nextColLength + 1):
            arr[row][col] = (arr[prevRow][col - 1] + 2 * prevRow * arr[prevRow][col]) % mod
    return arr[n][count]
