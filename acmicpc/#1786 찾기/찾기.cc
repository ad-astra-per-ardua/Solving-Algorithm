#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<int> getPi(const string& P) {
    vector<int> pi(P.size(), 0);
    int j = 0;
    
    for (int i = 1; i < P.size(); i++) {
        while (j > 0 && P[i] != P[j]) {
            j = pi[j - 1];
        }
        if (P[i] == P[j]) {
            j++;
            pi[i] = j;
        }
    }
    return pi;
}

void KMP(const string& T, const string& P, const vector<int>& pi) {
    vector<int> result;
    int cnt = 0;
    int j = 0;
    for (int i = 0; i < T.size(); i++) {
        while (j > 0 && T[i] != P[j]) {
            j = pi[j - 1];
        }
        if (T[i] == P[j]) {
            if (j == (P.size() - 1)) {
                result.push_back(i - P.size() + 2);
                cnt++;
                j = pi[j];
            } else {
                j++;
            }
        }
    }
    cout << cnt << "\n";
    for (const auto& r : result) {
        cout << r << "\n";
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string T, P;
    getline(cin, T);
    getline(cin, P);
    vector<int> pi = getPi(P);
    KMP(T, P, pi);

    return 0;
}
