#include <iostream>

using namespace std;

void solve1(int row, int col, int ld, int rd, int n, int& count) {
    if (row == n) {
        count++;
        return;
    }

    int pos = ((1 << n) - 1) & (~(col | ld | rd));
    while (pos) {
        int p = pos & -pos;
        pos -= p;
        solve1(row + 1, col | p, (ld | p) << 1, (rd | p) >> 1, n, count);
    }
}

int solution(int n) {
    int count = 0;
    solve1(0, 0, 0, 0, n, count);
    return count;
}

