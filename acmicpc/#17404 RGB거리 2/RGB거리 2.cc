#include <iostream>
#include <algorithm>
#include <cstring>
#define MAX 1001

using namespace std;

int n;
int cost[MAX][3];
int dp[MAX][3][3];

int solve(int pos, int first, int color) {
    if(pos == n) {
        if(first == color) return 1e9;
        return cost[pos][color];
    }
    int &ret = dp[pos][first][color];
    if(ret != -1) return ret;

    ret = 1e9;
    for(int i=0; i<3; i++) {
        if(color == i) continue;
        ret = min(ret, solve(pos+1, first, i) + cost[pos][color]);
    }
    return ret;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;
    for(int i=1; i<=n; i++){
        cin >> cost[i][0] >> cost[i][1] >> cost[i][2];
    }

    int ans = 1e9;
    for(int i=0; i<3; i++) {
        memset(dp, -1, sizeof(dp));
        ans = min(ans, solve(1, i, i));
    }

    cout << ans;

    return 0;
}
