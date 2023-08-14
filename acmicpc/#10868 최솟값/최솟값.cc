#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

int N, M;
vector<int> arr;

int minimum(int left, int right, int node_left, int node_right, int node_num) {
    if (left > node_right || right < node_left) return 1000000000;
    if (left <= node_left && right >= node_right) return arr[node_num];
    int mid = (node_left + node_right) / 2;
    return min(minimum(left, right, node_left, mid, node_num*2),
               minimum(left, right, mid+1, node_right, node_num*2 + 1));
}

void init(int size) {
    for (int i = size - 1; i > 0; i--) {
        arr[i] = min(arr[i*2], arr[i*2 + 1]);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M;

    int size = 2 << (int)ceil(log2(N)-1);
    int size_max = size * 2;
    arr.resize(size_max, 1000000000);

    for (int i = 0; i < N; i++) {
        cin >> arr[size+i];
    }

    init(size);

    for (int i = 0; i < M; i++) {
        int s, e;
        cin >> s >> e;
        cout << minimum(s-1, e-1, 0, size - 1, 1) << '\n';
    }

    return 0;
}
