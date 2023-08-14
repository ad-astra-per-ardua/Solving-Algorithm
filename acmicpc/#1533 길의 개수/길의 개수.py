import sys
input = sys.stdin.readline
mod = 1000003

class Matrix:
    def __init__(self, size=0):
        self.size = size
        self.arr = [[0 for _ in range(size)] for _ in range(size)]

    def multiply(self, other):
        result = Matrix(self.size)
        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    result.arr[i][j] += self.arr[i][k] * other.arr[k][j]
                    result.arr[i][j] %= mod
        return result


def powmat(a, b):
    if b == 1:
        return a
    ret = powmat(a, b // 2)
    ret = ret.multiply(ret)
    if b & 1:
        ret = ret.multiply(a)
    return ret


if __name__ == '__main__':
    n, s, e, t = map(int, input().split())
    s -= 1
    e -= 1
    mat = Matrix(n * 5)
    for i in range(n):
        for j in range(1, 5):
            mat.arr[i * 5 + j][i * 5 + j - 1] = 1

    for i in range(n):
        row = input().strip()
        for j in range(n):
            time = int(row[j])
            if time == 1:
                mat.arr[i * 5][j * 5] = 1
            elif time > 1:
                mat.arr[i * 5][j * 5 + time - 1] = 1

    ans = powmat(mat, t)
    print(ans.arr[s * 5][e * 5])
