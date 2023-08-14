#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>

using namespace std;

int n, m;
vector<vector<int>> graph;
vector<vector<bool>> visited;
pair<int, int> dir[4] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
set<tuple<int, int, int>> edge;

bool condition(int ni, int nj) {
    return ni < 0 || ni >= n || nj < 0 || nj >= m;
}

void marking(int y, int x, int mark) {
    queue<pair<int, int>> q;
    q.push({y, x});
    graph[y][x] = mark;
    visited[y][x] = true;

    while (!q.empty()) {
        int i, j;
        tie(i, j) = q.front(); q.pop();

        for (auto [dy, dx] : dir) {
            int ni = i + dy, nj = j + dx;
            if (condition(ni, nj) || !graph[ni][nj] || visited[ni][nj]) continue;
            graph[ni][nj] = mark;
            visited[ni][nj] = true;
            q.push({ni, nj});
        }
    }
}

void getDist(int y, int x, int now) {
    queue<tuple<int, int, int, pair<int, int>>> q;

    for (int idx = 0; idx < 4; idx++) {
        q.push({y, x, 0, dir[idx]});
    }

    while (!q.empty()) {
        int i, j, cnt;
        pair<int, int> nowDir;
        tie(i, j, cnt, nowDir) = q.front(); q.pop();

        if (graph[i][j] != 0 && graph[i][j] != now) {
            if (cnt > 2) {
                edge.insert({cnt - 1, now, graph[i][j]});
            }
            continue;
        }

        int ni = i + nowDir.first, nj = j + nowDir.second;
        if (condition(ni, nj) || graph[ni][nj] == now) continue;
        q.push({ni, nj, cnt + 1, nowDir});
    }
}

int findParent(vector<int>& parent, int x) {
    if (x != parent[x]) {
        parent[x] = findParent(parent, parent[x]);
    }
    return parent[x];
}

void unionParent(vector<int>& parent, int a, int b) {
    a = findParent(parent, a);
    b = findParent(parent, b);
    if (a > b) {
        parent[b] = parent[a];
    } else {
        parent[a] = parent[b];
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    cin >> n >> m;
    graph.resize(n, vector<int>(m));
    visited.resize(n, vector<bool>(m, false));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> graph[i][j];
        }
    }

    int mark = 1;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (graph[i][j] && !visited[i][j]) {
                marking(i, j, mark);
                mark++;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (graph[i][j] != 0) {
                visited.assign(n, vector<bool>(m, false));
                getDist(i, j, graph[i][j]);
            }
        }
    }

    vector<tuple<int, int, int>> edgeList(edge.begin(), edge.end());
    sort(edgeList.begin(), edgeList.end());

    vector<int> parent(mark);
    for (int i = 0; i < mark; i++) {
        parent[i] = i;
    }

    int result = 0, num = 0;
    for (auto [cost, a, b] : edgeList) {
        if (findParent(parent, a) != findParent(parent, b)) {
            num++;
            unionParent(parent, a, b);
            result += cost;
        }
    }

    if (result == 0 || num != mark - 2) {
        cout << -1 << "\n";
    } else {
        cout << result << "\n";
    }

    return 0;
}
