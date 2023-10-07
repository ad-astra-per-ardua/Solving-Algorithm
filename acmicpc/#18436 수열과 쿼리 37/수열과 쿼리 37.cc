#include <iostream>
#include <vector>
using namespace std;

int N;
vector<pair<int, int>> tree;
vector<int> L;
pair<int, int> init(int node, int start, int end) {
    if (start == end) {
        if (L[start] % 2 == 0) {
            tree[node].first = 1;
        } else {
            tree[node].second = 1;
        }
    } else {
        int mid = (start + end) / 2;
        pair<int, int> left_result = init(2 * node, start, mid);
        pair<int, int> right_result = init(2 * node + 1, mid + 1, end);
        
        tree[node].first = left_result.first + right_result.first;
        tree[node].second = left_result.second + right_result.second;
    }
    return tree[node];
}

void update(int node, int start, int end, int index, int value) {
    if (index < start || index > end) return;
    if (start == end) {
        if (value % 2 == 0) {
            tree[node] = {1, 0};
        } else {
            tree[node] = {0, 1};
        }
        return;
    }
    int mid = (start + end) / 2;
    update(2 * node, start, mid, index, value);
    update(2 * node + 1, mid + 1, end, index, value);
    tree[node].first = tree[2 * node].first + tree[2 * node + 1].first;
    tree[node].second = tree[2 * node].second + tree[2 * node + 1].second;
}
pair<int, int> query(int node, int start, int end, int left, int right) {
    if (left > end || right < start) return {0, 0};

    if (left <= start && right >= end) return tree[node];

    int mid = (start + end) / 2;
    pair<int, int> left_result = query(2 * node, start, mid, left, right);
    pair<int, int> right_result = query(2 * node + 1, mid + 1, end, left, right);

    return {left_result.first + right_result.first, left_result.second + right_result.second};
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> N;
    tree.resize(4 * N, {0, 0});
    L.resize(N);
    for (int i = 0; i < N; i++) {
        cin >> L[i];
    }
    init(1, 0, N - 1);
    int Q;
    cin >> Q;
    while (Q--) {
        int cmd, A, B;
        cin >> cmd >> A >> B;
        if (cmd == 1) {
            if (L[A - 1] % 2 == B % 2) {
                L[A - 1] = B;
            } else {
                update(1, 0, N - 1, A - 1, B);
                L[A - 1] = B;
            }
        } else if (cmd == 2) {
            cout << query(1, 0, N - 1, A - 1, B - 1).first << "\n";
        } else {
            cout << query(1, 0, N - 1, A - 1, B - 1).second << "\n";
        }
    }
    return 0;
}
