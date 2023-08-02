#include <vector>
#include <queue>
#include <cstring>
#include <limits>

using namespace std;
const int INF = numeric_limits<int>::max();

struct Edge {
    int to, cap, cost, rev;
};

struct MCMF {
    int size, src, sink;
    vector<vector<Edge>> graph;
    vector<int> dist, parent, edgeIdx;
    MCMF(int size, int src, int sink) : size(size), src(src), sink(sink), graph(size), dist(size), parent(size), edgeIdx(size) {}
    
    void addEdge(int from, int to, int cap, int cost) {
        graph[from].push_back({to, cap, cost, (int)graph[to].size()});
        graph[to].push_back({from, 0, -cost, (int)graph[from].size() - 1});
    }

    bool spfa() {
        vector<bool> inQ(size, false);
        queue<int> q;
        fill(dist.begin(), dist.end(), INF);
        dist[src] = 0;
        q.push(src);
        while (!q.empty()) {
            int here = q.front(); q.pop();
            inQ[here] = false;
            for (int i = 0; i < graph[here].size(); ++i) {
                Edge& e = graph[here][i];
                if (e.cap > 0 && dist[here] + e.cost < dist[e.to]) {
                    dist[e.to] = dist[here] + e.cost;
                    parent[e.to] = here;
                    edgeIdx[e.to] = i;
                    if (!inQ[e.to]) {
                        q.push(e.to);
                        inQ[e.to] = true;
                    }
                }
            }
        }
        return dist[sink] != INF;
    }

    pair<int, int> getMCMF() {
        int maxFlow = 0, minCost = 0;
        while (spfa()) {
            int flow = INF, costSum = 0;
            for (int p = sink; p != src; p = parent[p]) {
                Edge& e = graph[parent[p]][edgeIdx[p]];
                flow = min(flow, e.cap);
                costSum += e.cost;
            }
            for (int p = sink; p != src; p = parent[p]) {
                Edge& e = graph[parent[p]][edgeIdx[p]];
                e.cap -= flow;
                graph[e.to][e.rev].cap += flow;
            }
            maxFlow += flow;
            minCost += flow * costSum;
        }
        return {maxFlow, minCost};
    }
};

vector<int> treeOne[103], treeTwo[103];
int dp[103][103];

int traverse(int cur1, int prev1, int cur2, int prev2) {
    int& cache = dp[cur1][cur2];
    if (cache != -1) return cache;
    int num1 = treeOne[cur1].size(), num2 = treeTwo[cur2].size();
    int src = num1 + num2, sink = src + 1;
    MCMF mcmf(2 + num1 + num2, src, sink);
    for (int i = 0; i < num1; ++i) {
        int u = treeOne[cur1][i];
        if (u == prev1) continue;
        for (int j = 0; j < num2; ++j) {
            int v = treeTwo[cur2][j];
            if (v == prev2) continue;
            int cost = traverse(u, cur1, v, cur2);
            mcmf.addEdge(i, num1 + j, 1, -cost);
        }
        mcmf.addEdge(src, i, 1, 0);
    }
    for (int i = 0; i < num2; ++i) {
        mcmf.addEdge(num1 + i, sink, 1, 0);
    }
    int result = -mcmf.getMCMF().second + 1;
    return cache = result;
}

int solution(int n1, vector<vector<int>> edges1, int n2, vector<vector<int>> edges2) {
    memset(dp, -1, sizeof(dp));
    for (int i = 0; i < 103; ++i) treeOne[i].clear(), treeTwo[i].clear();
    for (auto edge : edges1) {
        int a = edge[0], b = edge[1];
        treeOne[a].push_back(b);
        treeOne[b].push_back(a);
    }
    for (auto edge : edges2) {
        int a = edge[0], b = edge[1];
        treeTwo[a].push_back(b);
        treeTwo[b].push_back(a);
    }
    return traverse(1, 0, 1, 0);
}
