#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;
    cin >> n >> k;

    vector<pair<int, int>> gems(n);
    for(int i=0; i<n; i++)
        cin >> gems[i].first >> gems[i].second;

    vector<int> bags(k);
    for(int i=0; i<k; i++)
        cin >> bags[i];

    sort(gems.begin(), gems.end());
    sort(bags.begin(), bags.end());

    long long result = 0;
    priority_queue<int> tmp;

    for(int i=0, j=0; i<k; i++) {
        while(j < n && gems[j].first <= bags[i]) {
            tmp.push(gems[j++].second);
        }
        if(!tmp.empty()) {
            result += tmp.top();
            tmp.pop();
        }
    }
    cout << result << '\n';

    return 0;
}
