#include <iostream>
#include <vector>
#include <queue>
#include <limits>
#include <tuple>

using namespace std;

vector<vector<int>> dijkstra(vector<vector<pair<int, int>>> &graph, vector<int> &costlist, int s) {
    int n = static_cast<int>(graph.size());
    vector<vector<int>> minload(n);
    queue<pair<int, int>> q;
    costlist[s] = 0;
    q.push({s, 0});

    while (!q.empty()) {
        int node, cost;
        tie(node, cost) = q.front(); q.pop();
        if (cost > costlist[node]) continue;
        for (auto &e : graph[node]) {
            int nnode = e.first;
            int ncost = e.second;
            if (ncost != -1 && costlist[nnode] > costlist[node] + ncost) {
                costlist[nnode] = costlist[node] + ncost;
                minload[nnode].clear();
                minload[nnode].push_back(node);
                q.push({nnode, ncost});
            } else if (costlist[nnode] == costlist[node] + ncost) {
                minload[nnode].push_back(node);
            }
        }
    }
    return minload;
}

void bfs(int d, vector<vector<int>> &minload, vector<bool> &visit, vector<vector<pair<int, int>>> &graph) {
    queue<int> q;
    q.push(d);
    visit[d] = true;

    while (!q.empty()) {
        int node = q.front(); q.pop();
        for (int nnode : minload[node]) {
            if (!visit[nnode]) {
                q.push(nnode);
                visit[nnode] = true;
            }
            for (auto &e : graph[nnode]) {
                if (e.first == node) {
                    e.second = -1;
                }
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    while (true) {
        int n, m;
        cin >> n >> m;
        if (n == 0 && m == 0) break;
        
        vector<vector<pair<int, int>>> graph(n);
        int s, d;
        cin >> s >> d;
        for (int i = 0; i < m; i++) {
            int u, v, p;
            cin >> u >> v >> p;
            graph[u].push_back({v, p});
        }

        vector<int> costlist(n, numeric_limits<int>::max());
        auto minload = dijkstra(graph, costlist, s);
        vector<bool> visit(n, false);
        bfs(d, minload, visit, graph);
        costlist.assign(n, numeric_limits<int>::max());
        dijkstra(graph, costlist, s);

        if (costlist[d] == numeric_limits<int>::max()) {
            cout << -1 << '\n';
        } else {
            cout << costlist[d] << '\n';
        }
    }

    return 0;
}
