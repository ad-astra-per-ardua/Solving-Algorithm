#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T, a, b;
    cin >> T;

    vector<pair<int, int>> L(T);
    for(int i = 0; i < T; i++) {
        cin >> a >> b;
        L[i] = {a, b};
    }
    
    sort(L.begin(), L.end());

    vector<int> dp, A_line;
    vector<pair<int, int>> check;
    for(auto& i : L) {
        if(dp.empty() || dp.back() < i.second) {
            dp.push_back(i.second);
            check.push_back({dp.size() - 1, i.second});
        } else {
            auto index = lower_bound(dp.begin(), dp.end(), i.second) - dp.begin();
            dp[index] = i.second;
            check.push_back({index, i.second});
        }
    }

    vector<int> answer;
    int last_index = dp.size() - 1;
    for(int i = check.size() - 1; i >= 0; i--) {
        if(check[i].first == last_index) {
            answer.push_back(check[i].second);
            last_index--;
        }
    }

    cout << T - dp.size() << "\n";

    for(int i = T - 1; i >= 0; i--) {
        for(auto& j : answer) {
            if(L[i].second == j) {
                A_line.push_back(L[i].first);
                break;
            }
        }
    }

    sort(A_line.begin(), A_line.end());

    int count = 0;
    for(int i = 0; i < T; i++) {
        bool P = false;
        for(auto& j : A_line) {
            if(L[i].first == j) {
                P = true;
                break;
            }
        }
        if(!P) {
            cout << L[i].first << "\n";
        }
    }

    return 0;
}
