#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    vector<int> mem(N + 1, 0);
    vector<string> path(N + 1, "");

    path[1] = "1";

    for (int idx = 2; idx <= N; ++idx) {
        mem[idx] = mem[idx - 1] + 1;
        int prev = idx - 1;
        
        if (idx % 3 == 0 && mem[idx / 3] + 1 < mem[idx]) {
            mem[idx] = mem[idx / 3] + 1;
            prev = idx / 3;
        }

        if (idx % 2 == 0 && mem[idx / 2] + 1 < mem[idx]) {
            mem[idx] = mem[idx / 2] + 1;
            prev = idx / 2;
        }
        
        path[idx] = to_string(idx) + " " + path[prev];
    }

    cout << mem[N] << "\n";
    cout << path[N] << "\n";

    return 0;
}
