#include <vector>
#include <algorithm>

using namespace std;

const int INF = 987654321;

int solution(int n, int m, vector<vector<int>> edges, int k, vector<int> gps) {
    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<vector<int>> dp(k, vector<int>(n + 1, INF));
    dp[0][gps[0]] = 0;

    for (int i = 1; i < k; ++i) {
        for (int j = 1; j <= n; ++j) {
            dp[i][j] = min(dp[i - 1][j], dp[i][j]);
            for (int a : adj[j])
                dp[i][j] = min(dp[i - 1][a], dp[i][j]);
            dp[i][j] += (gps[i] != j);
        }
    }

    return dp[k - 1][gps[k - 1]] < INF ? dp[k - 1][gps[k - 1]] : -1;
}
