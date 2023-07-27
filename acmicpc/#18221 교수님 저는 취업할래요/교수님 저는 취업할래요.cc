#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N;
    cin >> N;

    vector<vector<int>> array(N, vector<int>(N));
    pair<int, int> teacher;
    pair<int, int> seungue;

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> array[i][j];
            if (array[i][j] == 5) {
                teacher = make_pair(i, j);
            }
            else if (array[i][j] == 2) {
                seungue = make_pair(i, j);
            }
        }
    }

    auto getRectangle = [&]() {
        return make_pair(make_pair(min(teacher.first, seungue.first), max(teacher.first, seungue.first)),
                         make_pair(min(teacher.second, seungue.second), max(teacher.second, seungue.second)));
    };

    auto isDistMoreThan5 = [&]() {
        int dx = teacher.first - seungue.first;
        int dy = teacher.second - seungue.second;
        return sqrt(dx * dx + dy * dy) >= 5;
    };

    if (isDistMoreThan5()) {
        auto rectangle = getRectangle();
        int count = 0;
        for (int i = rectangle.first.first; i <= rectangle.first.second; ++i) {
            for (int j = rectangle.second.first; j <= rectangle.second.second; ++j) {
                if (array[i][j] == 1) {
                    ++count;
                }
                if (count >= 3) {
                    break;
                }
            }
            if (count >= 3) {
                break;
            }
        }
        cout << (count >= 3 ? 1 : 0);
    }
    else {
        cout << 0;
    }

    return 0;
}
