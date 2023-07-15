#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    vector<int> array(n);
    for(int i = 0; i < n; ++i) {
        cin >> array[i];
    }

    sort(array.begin(), array.end());

    int maxCount = 0, mode = array[0], currCount = 0;
    for(int i = 0; i < n; ++i) {
        if (array[i] == array[i-1]) {
            currCount++;
        } else {
            currCount = 1;
        }
        
        if (currCount > maxCount) {
            maxCount = currCount;
            mode = array[i];
        }
    }

    cout << mode;

    return 0;
}
