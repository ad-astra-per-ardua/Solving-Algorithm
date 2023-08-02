#include <iostream>
#include <vector>
using namespace std;

const int MOD = 1000000000;
const int MAX = (1 << 10) - 1;

int get_stair_count(int N) {
    vector<vector<int>> dp(10, vector<int>(MAX + 1, 0));

    for (int i = 1; i < 10; ++i) {
        dp[i][1 << i] = 1;
    }

    for (int _ = 2; _ <= N; ++_) {
        vector<vector<int>> next_dp(10, vector<int>(MAX + 1, 0));

        for (int i = 0; i < 10; ++i) {
            for (int j = 0; j <= MAX; ++j) {
                if (i > 0) {
                    next_dp[i][j | (1 << i)] = (next_dp[i][j | (1 << i)] + dp[i - 1][j]) % MOD;
                }
                if (i < 9) {
                    next_dp[i][j | (1 << i)] = (next_dp[i][j | (1 << i)] + dp[i + 1][j]) % MOD;
                }
            }
        }

        dp = next_dp;
    }

    int sum = 0;
    for (int i = 0; i < 10; ++i) {
        sum = (sum + dp[i][MAX]) % MOD;
    }

    return sum;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    cout << get_stair_count(N) << '\n';

    return 0;
}
