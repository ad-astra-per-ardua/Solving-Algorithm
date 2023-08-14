#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<pair<int, int>> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i].first >> arr[i].second;
        if (arr[i].first > arr[i].second) {
            swap(arr[i].first, arr[i].second);
        }
    }

    sort(arr.begin(), arr.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
        return a.second < b.second;
    });

    int d;
    cin >> d;

    vector<pair<int, int>> h_o;
    for (const auto& l : arr) {
        if (l.second - l.first <= d) {
            h_o.push_back(l);
        }
    }

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> heap;
    int cnt = 0;
    for (const auto& l : h_o) {
        while (!heap.empty() && heap.top().first < l.second - d) {
            heap.pop();
        }
        heap.push(l);
        cnt = max(cnt, (int)heap.size());
    }

    cout << cnt << endl;
    return 0;
}
