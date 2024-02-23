#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

vector<vector<int>> graph;
vector<bool> visited_dfs, visited_bfs;

void dfs(int v) {
    visited_dfs[v] = true;
    cout << v << ' ';
    for (int i = 1; i <= graph.size() - 1; ++i) {
        if (!visited_dfs[i] && graph[v][i] == 1) {
            dfs(i);
        }
    }
}

void bfs(int v) {
    queue<int> q;
    q.push(v);
    visited_bfs[v] = true;
    while (!q.empty()) {
        int e = q.front();
        q.pop();
        cout << e << ' ';
        for (int i = 1; i <= graph.size() - 1; ++i) {
            if (!visited_bfs[i] && graph[e][i] == 1) {
                q.push(i);
                visited_bfs[i] = true;
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m, v;
    cin >> n >> m >> v;

    graph.resize(n + 1, vector<int>(n + 1, 0));
    visited_dfs.resize(n + 1, false);
    visited_bfs.resize(n + 1, false);

    for (int i = 0; i < m; ++i) {
        int x, y;
        cin >> x >> y;
        graph[x][y] = 1;
        graph[y][x] = 1;
    }

    dfs(v);
    cout << endl;
    bfs(v);

    return 0;
}
