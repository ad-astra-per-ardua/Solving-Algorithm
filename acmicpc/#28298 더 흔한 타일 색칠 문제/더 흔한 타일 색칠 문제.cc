#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M, K, Sum = 0;
    cin >> N >> M >> K;
    vector<vector<char>> tiles(N, vector<char>(M));
    vector<int> count_list(26);

    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
            cin >> tiles[i][j];

    int step_num = N * M / (K * K);

    for (int x = 0; x < K; x++) {
        for (int y = 0; y < K; y++) {

            fill(count_list.begin(), count_list.end(), 0);

            for (int i = 0; i < N - K + 1; i += K) {
                for (int j = 0; j < M - K + 1; j += K) {
                    char t = tiles[i + x][j + y];
                    count_list[t - 'A']++;
                }
            }

            int max_tile_num = *max_element(count_list.begin(), count_list.end());
            Sum += step_num - max_tile_num;
            char max_tile = distance(count_list.begin(), max_element(count_list.begin(), count_list.end())) + 'A';

            for (int i = 0; i < N - K + 1; i += K) {
                for (int j = 0; j < M - K + 1; j += K) {
                    tiles[i + x][j + y] = max_tile;
                }
            }
        }
    }

    cout << Sum << '\n';
    for (const auto& line : tiles) {
        for (const auto& tile : line) {
            cout << tile;
        }
        cout << '\n';
    }

    return 0;
}
