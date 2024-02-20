#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<int> A(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    vector<int> array;
    array.push_back(A[0]);

    for (int i = 0; i < N; ++i) {
        if (array.back() < A[i]) {
            array.push_back(A[i]);
        } else {
            auto it = lower_bound(array.begin(), array.end(), A[i]);
            *it = A[i];
        }
    }

    cout << array.size() << '\n';

    return 0;
}
