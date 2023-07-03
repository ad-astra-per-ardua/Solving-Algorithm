#include <iostream>
#include <algorithm>
#define MAX 100001
using namespace std;

int N, S;
int arr[MAX];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> S;
    for (int i = 0; i < N; i++) cin >> arr[i];

    int low = 0, high = 0, sum = arr[0], result = MAX;

    while (low <= high && high < N) {
        if (sum < S) sum += arr[++high];
        else {
            result = min(result, (high - low + 1));
            sum -= arr[low++];
        }
    }

    if(result != MAX) cout << result;
    else cout << 0;

    return 0;
}
