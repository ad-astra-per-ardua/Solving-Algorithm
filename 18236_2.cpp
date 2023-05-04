#include <iostream>
#include <vector>
#include <limits>

using namespace std;

int matrix_chain_order(const vector<pair<int, int>>& matrices) {
    int n = matrices.size();
    vector<vector<int>> m(2, vector<int>(n, 0));

    for (int len = 1; len < n; ++len) {
        for (int i = 0; i < n - len; ++i) {
            int j = i + len;
            m[1][j] = numeric_limits<int>::max();
            for (int k = i; k < j; ++k) {
                int cost = m[0][k] + m[0][j] + matrices[i].first * matrices[k].second * matrices[j].second;
                m[1][j] = min(m[1][j], cost);
            }
        }
        m[0] = m[1];
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
