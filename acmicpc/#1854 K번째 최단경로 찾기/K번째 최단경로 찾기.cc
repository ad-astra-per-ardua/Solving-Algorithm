#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <climits>

using namespace std;

int N, M, K;
vector<pair<int, int>> weight[100001];
vector<vector<int>> distTable;

void dijkstra(int start) {
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> heap;
    heap.push({0, start});
    distTable[start][0] = 0;

    while (!heap.empty()) {
        int cost = heap.top().first;
        int curr = heap.top().second;
        heap.pop();

        for (auto [nextNode, c] : weight[curr]) {
            int w = cost + c;
            if (w < distTable[nextNode][K-1]) {
                distTable[nextNode][K-1] = w;
                sort(distTable[nextNode].begin(), distTable[nextNode].end());
                heap.push({w, nextNode});
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M >> K;

    distTable.resize(N+1, vector<int>(K, INT_MAX));

    for (int i = 0; i < M; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        weight[a].push_back({b, c});
    }

    dijkstra(1);

    for (int i = 1; i <= N; i++) {
        if (distTable[i][K-1] == INT_MAX) {
            cout << "-1\n";
        } else {
            cout << distTable[i][K-1] << "\n";
        }
    }

    return 0;
}
