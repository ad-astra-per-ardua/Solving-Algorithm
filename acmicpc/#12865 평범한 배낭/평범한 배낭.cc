#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, k;
    cin >> n >> k;
    vector<pair<int, int>> put(n + 1, {0, 0});
    vector<vector<int>> bag(n + 1, vector<int>(k + 1, 0));

    for (int i = 1; i <= n; ++i) {
        cin >> put[i].first >> put[i].second;
    }
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= k; ++j) {
            int kg = put[i].first;
            int val = put[i].second;
            if (j < kg) {
                bag[i][j] = bag[i - 1][j];
            } else {
                bag[i][j] = max(val + bag[i - 1][j - kg], bag[i - 1][j]);
            }
        }
    }
    cout << bag[n][k] << endl;

    return 0;
}
