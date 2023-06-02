#include <bits/stdc++.h>
using namespace std;

const int N = 1e6 + 50;

int n, m, k, a[N], b[N], l[N], arr[N], vis[N];

constexpr int lowbit(int x) { return x & -x; }

struct tree_t {
	int t[N];
	inline void clear(int n) {
		for (int i = 0; i <= n;++i) t[i] = 0;
	}
	inline void add(int p, int v) {
		for (; p <= n; p += lowbit(p))
			t[p] += v;
	}
	inline int qry(int p) {
		int r = 0;
		for (; p; p -= lowbit(p))
			r += t[p];
		return r;
	}
} tr;

bool work() {
	cin >> n >> m >> k;
	for (int i = 1; i <= n; ++i) {
		vis[i] = false;
	}
	for (int i = 1; i <= n; ++i) {
		cin >> a[i];
		arr[a[i]] = i;
	}
	for (int i = 1; i <= m; ++i) {
		cin >> b[i];
	}
	for (int i = 1; i <= k; ++i) {
		cin >> l[i];
	}
	tr.clear(n);
	bool t = true;
	int p = 0;
	for (int i = 1; i <= m; ++i) {
		if (arr[b[i]] < arr[p])
			return false;
		vis[b[i]] = true;
		p = b[i];
	}
	set<int> se = {0, n + 1};
	priority_queue<int> Lq;
	for (int i = 1; i <= k; ++i)
		Lq.emplace(l[i]);
	vector<int> ret;
	for (int i = n; i >= 1; --i)
		if (vis[i]) {
			se.emplace(arr[i]);
		}
		else {
			auto it = se.lower_bound(arr[i]);
			tr.add(arr[i], 1);
			int v = *it - *prev(it);
			v -= tr.qry(*it - 1);
			v += tr.qry(*prev(it));
			ret.emplace_back(v);
		}
	sort(ret.begin(), ret.end(), greater<int>());
	for (int y : ret) {
		while (!Lq.empty() && Lq.top() > y)
			Lq.pop();
		if (Lq.empty()) return false;
		Lq.pop();
	}
	return true;

}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	int T;
	cin >> T;
	while (T--) {
		cout << (work() ? "YES" : "NO") << '\n';
	}
}
