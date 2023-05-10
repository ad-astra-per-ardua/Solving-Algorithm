#include <iostream>
#include <vector>
#include <algorithm>
#include <tuple>
using namespace std;

int find_largest_lake(vector<vector<int>>& grid) {
    int n = grid.size(), m = grid[0].size();
    vector<vector<bool>> visited(n, vector<bool>(m, false));

    auto dfs = [&](int i, int j) {
        vector<pair<int, int>> stack = {{i, j}};
        int volume = 0;
        while (!stack.empty()) {
            tie(i, j) = stack.back();
            stack.pop_back();
            if (!visited[i][j]) {
                visited[i][j] = true;
                if (grid[i][j] == 0) {
                    continue;
                }
                volume += grid[i][j];
                vector<pair<int, int>> directions = {{i-1, j}, {i+1, j}, {i, j-1}, {i, j+1}};
                for (const auto& [ni, nj] : directions) {
                    if (0 <= ni && ni < n && 0 <= nj && nj < m && !visited[ni][nj]) {
                        stack.push_back({ni, nj});
                    }
                }
            }
        }
        return volume;
    };

    int max_lake_volume = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (!visited[i][j]) {
                max_lake_volume = max(max_lake_volume, dfs(i, j));
            }
        }
    }

    return max_lake_volume;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int t;
    scanf("%d", &t);
    for (int _ = 0; _ < t; ++_) {
        int n, m;
        scanf("%d %d", &n, &m);
        vector<vector<int>> grid(n, vector<int>(m));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                scanf("%d", &grid[i][j]);
            }
        }
        printf("%d\n", find_largest_lake(grid));
    }
    return 0;
}
