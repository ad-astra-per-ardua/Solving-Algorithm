#include <iostream>
#include <vector>
#include <limits>

using namespace std;

int matrix_chain_order(const vector<pair<int, int>>& matrices) {
    int n = matrices.size();
    vector<vector<int>> m(n, vector<int>(n, 0));
    vector<vector<int>> s(n, vector<int>(n, 0));

    for (int len = 1; len < n; ++len) {
        for (int i = 0; i < n - len; ++i) {
            int j = i + len;
            m[i][j] = numeric_limits<int>::max();
            for (int k = s[i][j - 1]; k <= s[i + 1][j]; ++k) {
                int cost = m[i][k] + m[k + 1][j] + matrices[i].first * matrices[k].second * matrices[j].second;
                if (cost < m[i][j]) {
                    m[i][j] = cost;
                    s[i][j] = k;
                }
            }
        }
    }

    return m[0][n - 1];
}

int main() {
    int N;
    cin >> N;
    vector<pair<int, int>> matrices(N);
    for (int i = 0; i < N; i++) {
        cin >> matrices[i].first >> matrices[i].second;
    }

    cout << matrix_chain_order(matrices) << endl;

    return 0;
}
