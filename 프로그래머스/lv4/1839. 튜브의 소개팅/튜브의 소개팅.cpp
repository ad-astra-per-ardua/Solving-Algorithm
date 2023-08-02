#include <vector>
#include <algorithm>
#include <iostream>
#include <cstring>

using namespace std;

pair<int, int> dir[4] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
vector<vector<int>> tm;
long long dp[50][50][2501];
int m, n, s;
long long MAX_VAL = 0x7FFFFFFF;

bool isValid(int x, int y) {
    return (0 <= x && x < m && 0 <= y && y < n);
}

long long getMin(int x, int y, int d) {
    long long &cur = dp[x][y][d];
    if(x == m - 1 && y == n - 1 && d == 0) 
        return cur = 0;
    if(cur != -1)
        return cur;
    
    cur = MAX_VAL;
    for(int i=0;i<4;i++) {
        int nx = x + dir[i].first;
        int ny = y + dir[i].second;
        if(!isValid(nx, ny) || tm[nx][ny] == -1 || d < 1)
            continue;
        long long res = getMin(nx, ny, d - 1) + tm[x][y];
        if(res <= s)
            cur = min(cur, res);
    }
    return cur;
}

vector<int> solution(int mVal, int nVal, int sVal, vector<vector<int>> time_map) {
    memset(dp, -1, sizeof(dp));
    tm = time_map;
    m = mVal; n = nVal; s = sVal;
    int min_dist = MAX_VAL;
    int min_time = MAX_VAL;
    
    for(int i = m + n - 2; i <= m * n; i++){
        long long res = getMin(0, 0, i); 
        if(res < MAX_VAL){
            min_dist = i;
            min_time = res;
            break;
        }
    }
    return vector<int>{min_dist, min_time};
}
