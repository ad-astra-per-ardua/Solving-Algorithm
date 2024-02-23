#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, K;
	cin >> N >> K;
	int l = 1, r = K;
	int ans = 1e9;
	while (l <= r) {
		int mid = (l + r) / 2;
		int cnt = 0;
		for (int i = 1; i <= N; i++) {
			cnt += min(mid / i,N);
		}
		if (cnt >= K) {
			r = mid - 1;
			ans = min(ans,mid);
		}
		else if(cnt < K) {
			l = mid + 1;
		}
	}
	cout << ans;
	return 0;
}
