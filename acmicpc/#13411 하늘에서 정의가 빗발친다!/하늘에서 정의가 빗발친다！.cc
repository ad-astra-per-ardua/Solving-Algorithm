#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

struct Robot {
    int num;
    double time;
    Robot(int num, int x, int y, int v) : num(num), time(sqrt(x*x + y*y) / v) {}
};

bool compare(Robot &r1, Robot &r2) {
    if (r1.time == r2.time)
        return r1.num < r2.num;
    return r1.time < r2.time;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;
    vector<Robot> robots;

    for (int i = 0; i < n; i++) {
        int x, y, v;
        cin >> x >> y >> v;
        robots.push_back(Robot(i, x, y, v));
    }

    sort(robots.begin(), robots.end(), compare);

    for (auto &robot : robots)
        cout << robot.num + 1 << '\n';

    return 0;
}
