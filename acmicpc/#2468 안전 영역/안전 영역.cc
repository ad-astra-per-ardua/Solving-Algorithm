#include <iostream>
#include <algorithm>
#include <cstring>
#define MAX 100
using namespace std;

int N, result;
int map[MAX][MAX];
bool visited[MAX][MAX];
int dx[4] = {-1, 0, 1, 0}, dy[4] = {0, 1, 0, -1};

void dfs(int x, int y, int h) {
    visited[x][y] = true;
    for(int i = 0; i < 4; i++) {
        int nx = x + dx[i], ny = y + dy[i];
        if(nx < 0 || ny < 0 || nx >= N || ny >= N) continue;
        if(!visited[nx][ny] && map[nx][ny] > h) dfs(nx, ny, h);
    }
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    cin >> N;
    int high = 0;
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            cin >> map[i][j];
            high = max(high, map[i][j]);
        }
    }

    for(int h = 0; h <= high; h++) { 
        memset(visited, false, sizeof(visited));
        int safe = 0;
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j++) {
                if(!visited[i][j] && map[i][j] > h) {
                    dfs(i, j, h);
                    safe++;
                }
            }
        }
        result = max(result, safe);
    }
    cout << result;
    return 0;
}
