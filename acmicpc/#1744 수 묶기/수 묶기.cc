#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);

    int N;
    cin >> N;

    priority_queue<int> plus;
    priority_queue<int, vector<int>, greater<int>> minus;
    int zeroCount = 0;
    long long result = 0;

    for (int i = 0; i < N; ++i) {
        int number;
        cin >> number;
        if (number == 1) result += 1;
        else if (number > 1) plus.push(number);
        else if (number == 0) zeroCount += 1;
        else minus.push(number);
    }

    while (plus.size() >= 2) {
        int first = plus.top();
        plus.pop();
        int second = plus.top();
        plus.pop();
        result += (first * second);
    }

    if (!plus.empty()) result += plus.top();

    while (minus.size() >= 2) {
        int first = minus.top();
        minus.pop();
        int second = minus.top();
        minus.pop();
        result += (first * second);
    }

    if (!minus.empty() && zeroCount == 0) result += minus.top();

    cout << result << "\n";

    return 0;
}
