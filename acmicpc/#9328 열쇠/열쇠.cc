#include <iostream>
#include <queue>
#include <vector>
#include <unordered_set>
#include <unordered_map>
using namespace std;

const vector<int> dy = {1, 0, -1, 0};
const vector<int> dx = {0, 1, 0, -1};

inline bool in_range(int y, int x, int h, int w) {
    return 0 <= y && y < h && 0 <= x && x < w;
}

inline int priority(char c, const unordered_set<char>& keys) {
    if (c == '$') return 0;
    if ('a' <= c && c <= 'z') return 1;
    if (c == '.') return 3;
    if ('A' <= c && c <= 'Z') {
        return keys.count(tolower(c)) ? 2 : 4;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        int h, w;
        cin >> h >> w;
        vector<string> board(h);
        for (string& row : board) cin >> row;

        string input_keys;
        cin >> input_keys;
        unordered_set<char> keys(input_keys.begin(), input_keys.end());

        unordered_map<char, vector<pair<int, int>>> found_locked_door;
        vector<vector<bool>> visit(h, vector<bool>(w));

        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<>> pq;

        int ans = 0;
        for (int i = 0; i < h; ++i) {
            for (int j = 0; j < w; ++j) {
                if ((i == 0 || i == h - 1 || j == 0 || j == w - 1) && board[i][j] != '*') {
                    int p = priority(board[i][j], keys);
                    if (p == 4) {
                        found_locked_door[board[i][j]].emplace_back(i, j);
                        continue;
                    }
                    pq.emplace(p, i, j);
                    visit[i][j] = true;
                }
            }
        }

        while (!pq.empty()) {
            auto [p, y, x] = pq.top();
            pq.pop();

            if (p == 0) {
                ++ans;
            } else if (p == 1) {
                keys.insert(board[y][x]);
                if (found_locked_door.count(toupper(board[y][x]))) {
                    for (auto [door_y, door_x] : found_locked_door[toupper(board[y][x])]) {
                        visit[door_y][door_x] = true;
                        pq.emplace(2, door_y, door_x);
                    }
                }
            }

            for (int i = 0; i < 4; ++i) {
                int ny = y + dy[i], nx = x + dx[i];
                if (in_range(ny, nx, h, w) && !visit[ny][nx] && board[ny][nx] != '*') {
                    int np = priority(board[ny][nx], keys);
                    if (np == 4) {
                        found_locked_door[board[ny][nx]].emplace_back(ny, nx);
                        continue;
                    }
                    visit[ny][nx] = true;
                    pq.emplace(np, ny, nx);
                }
            }
        }

        cout << ans << "\n";
    }

    return 0;
}
