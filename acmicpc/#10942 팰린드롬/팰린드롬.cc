#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;
    vector<int> num(n+1);
    for (int i = 1; i <= n; i++)
        cin >> num[i];

    vector<vector<int>> dp(n+1, vector<int>(n+1, 0));
    for (int i = 1; i <= n; i++) dp[i][i] = 1;
    for (int i = 1; i < n; i++)
        if (num[i] == num[i+1]) dp[i][i+1] = 1;

    for (int len = 3; len <= n; len++)
        for (int i = 1; i <= n - len + 1; i++) {
            int j = i + len - 1;
            if (num[i] == num[j] && dp[i+1][j-1]) dp[i][j] = 1;
        }

    int m;
    cin >> m;
    for (int i = 0; i < m; i++) {
        int s, e;
        cin >> s >> e;
        cout << dp[s][e] << '\n';
    }

    return 0;
}
