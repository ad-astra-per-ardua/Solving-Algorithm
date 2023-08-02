#include <map>
#include <string>
#include <vector>
#include <cstdio>
#include <cstring>
#include <cassert>
#include <algorithm>
 
using namespace std;

const long long mod = 1000000007;
const long long inf = mod * mod;
const int NSIZE = 200200;
 
 
class segtree {
public:
    int n;
    vector<long long> tree;

    void clear() {
        tree.clear();
    }

    int maxtree(int s, int e) {
        int now = 1;
        while (s != e) {
            s = (s + e) / 2 + 1;
            now = now * 2 + 1;
        }
        return now;
    }

    int maxtree(int s, int e, int now) {
        if (s == e) return now;
        return max(maxtree(s, (s + e) / 2, now * 2),
            maxtree((s + e) / 2 + 1, e, now * 2 + 1));
    }

    void init(int _n) {
        n = _n;
        tree.resize(maxtree(0, n, 1) + 10);
        fill(tree.begin(), tree.end(), 0);
    }

    void upd(int p, long long c) {
        this->update(0, n, 1, p, c);
    }

    long long update(int s, int e, int now, int p, long long c) {
        if (p < s || e < p) return tree[now];
        if (s == e) {
            return tree[now] = (tree[now] + c) % mod;
        }
        return tree[now] = (update(s, (s + e) / 2, now * 2, p, c) +
            update((s + e) / 2 + 1, e, now * 2 + 1, p, c)) % mod;
    }

    long long qry(int l, int r) {
        return this->query(0, n, 1, l, r) % mod;
    }

    long long query(int s, int e, int now, int l, int r) {
        if (r < l) return 0;
        if (r < s || e < l) return 0;
        if (l <= s && e <= r) return tree[now] % mod;
        return (query(s, (s + e) / 2, now * 2, l, r) +
            query((s + e) / 2 + 1, e, now * 2 + 1, l, r)) % mod;
    }
};

int dp[NSIZE], dp2[NSIZE];
vector<long long> lineVal;
vector<int> linelu[NSIZE], linerb[NSIZE];
vector<long long> luSum[NSIZE], luSum2[NSIZE], rbSum[NSIZE];
segtree rbSum2[NSIZE];
int lupos[NSIZE][2], rbpos[NSIZE][2];

void init(int n, vector<vector<int>> & point) {
    memset(dp, 0, sizeof(dp));
    memset(dp2, 0, sizeof(dp2));
    lineVal.clear();
    sort(point.begin(), point.end(), [](vector<int> a, vector<int> b) {
        return a[0] != b[0] ? a[0] < b[0] : a[1] != b[1] ? a[1] > b[1] : a[2] > b[2];
    });
    for (int i = 0; i<NSIZE; i++) {
        linelu[i].clear(); linerb[i].clear();
        luSum2[i].clear(); luSum[i].clear();
        rbSum[i].clear(); rbSum2[i].clear();
    }
    for (int i = 0; i<n; i++) {
        lineVal.push_back(0LL + point[i][0] - point[i][1]);
        lineVal.push_back(0LL + point[i][0] - point[i][1] - point[i][2]);
    }
    sort(lineVal.begin(), lineVal.end());
    lineVal.erase(unique(lineVal.begin(), lineVal.end()), lineVal.end());
    int lumin = 987654321;
    for (int i = 0; i<n; i++) {
        int idx; long long target = 0;
        target = point[i][0] - point[i][1];
        idx = lower_bound(lineVal.begin(), lineVal.end(), target) - lineVal.begin();
        assert(lineVal[idx] == target);
        linelu[idx].push_back(i);
        lupos[i][0] = idx; lupos[i][1] = linelu[idx].size() - 1;

        target = point[i][0] - point[i][1] - point[i][2];
        idx = lower_bound(lineVal.begin(), lineVal.end(), target) - lineVal.begin();
        assert(lineVal[idx] == target);
        linerb[idx].push_back(i);
        rbpos[i][0] = idx; rbpos[i][1] = linerb[idx].size() - 1;
    }
    for (int i = 0; i < NSIZE; i++) rbSum2[i].init(linerb[i].size());
    
    assert(linelu[lupos[0][0]].size() == 1);
    
    dp[0] = 1; luSum[lupos[0][0]].push_back(1);
    for (int i = 0; i<lineVal.size(); i++) {
        for (int j = 0; j<linelu[i].size(); j++) {
            int now = linelu[i][j];
            long long a = point[now][0], b = point[now][1], k = point[now][2];
            int p = lower_bound(lineVal.begin(), lineVal.end(), a - b - k) - lineVal.begin();
            assert(p == rbpos[now][0]);
            if (linelu[p].empty() || k == 1) continue;
            vector<int> temp = { (int)(a - (k - 1)), (int)(b + 1), 0 };
            int l = lower_bound(linelu[p].begin(), linelu[p].end(), temp, [&](int tt, vector<int> ss) { return point[tt] < ss; }) - linelu[p].begin();
            temp = { (int)(a - 1), (int)(b + k - 1), 1987654321 };
            int r = upper_bound(linelu[p].begin(), linelu[p].end(), temp, [&](vector<int> ss, int tt) { return ss < point[tt]; }) - linelu[p].begin();
            if (l >= r) continue;
            if (l >= 1) dp[now] = luSum[p][r - 1] - luSum[p][l - 1];
            else dp[now] = luSum[p][r - 1];
            dp[now] = (dp[now] + mod) % mod;
        }
        long long s = 0;
        for (int j = 0; j<linelu[i].size(); j++)
        {
            s += dp[linelu[i][j]];
            s %= mod;
            luSum[i].push_back(s);
        }
    }
    for (int i = 0; i<lineVal.size(); i++)
    {
        long long s = 0;
        for (int j = 0; j<linerb[i].size(); j++)
        {
            s += dp[linerb[i][j]];
            s %= mod;
            rbSum[i].push_back(s);
        }
    }
    assert(linelu[lupos[n - 1][0]].size() == 1);
    dp2[n - 1] = 1; luSum2[lupos[n - 1][0]].push_back(1);
    for (int i = lineVal.size() - 1; i >= 0; i--)
    {
        for (int j = 0; j<linelu[i].size(); j++)
        {
            int now = linelu[i][j];
            long long a = point[now][0], b = point[now][1], k = point[now][2];
            int p = lupos[now][0];
            if (linerb[p].empty()) continue;
            vector<int> temp = { (int)(a + 1), 0, 0 };
            int l = lower_bound(linerb[p].begin(), linerb[p].end(),
                temp, [&](int tt, vector<int> ss) {
                return ss > point[tt];
            }) - linerb[p].begin();
            int r = upper_bound(linerb[p].begin(), linerb[p].end(), b - 1, [&](int bb, int tt) {
                if (bb != point[tt][1]) return bb < point[tt][1];
                else return false;
            }) - linerb[p].begin();
            if (l >= r) continue;
            dp2[now] = rbSum2[p].qry(l, r) % mod;
        }
        long long s = 0;
        for (int j = 0; j<linelu[i].size(); j++)
        {
            s += dp2[linelu[i][j]];
            s %= mod;
            luSum2[i].push_back(s);
        }
        for (int j = 0; j<linelu[i].size(); j++) {
            int now = linelu[i][j];
            rbSum2[rbpos[now][0]].upd(rbpos[now][1], dp2[now]);
        }
    }
 
}
 
vector<int> solution(int n, vector<vector<int>> point, vector<vector<int>> query) {
    assert(point.size() == n);
    init(n, point);
    vector<int> answer;
    answer.push_back(dp[n - 1]);
    int cnt = -1;
    for (auto & q : query)
    {
        cnt++;
        int type; type = q[0];//scanf("%d", &type);
        long long a, b, k; a = q[1]; b = q[2];//scanf("%lld%lld", &a, &b);
        long long pre = 0, nxt = 0;
        if (type == 0) {
            k = q[3];//scanf("%lld", &k);
            int p = lower_bound(lineVal.begin(), lineVal.end(),
                a - b - k) - lineVal.begin();
            if (k != 1 && p < lineVal.size() && lineVal[p] == a - b - k && !linelu[p].empty())
            {
                vector<int> temp = { (int)(a - k + 1), (int)b + 1, 0 };
                int l = lower_bound(linelu[p].begin(), linelu[p].end(),
                    temp, [&](int tt, vector<int> ss) {
                    return point[tt] < ss;
                }) - linelu[p].begin();
                temp = { (int)(a - 1), (int)(b + k - 1), 1987654321 };
                int r = upper_bound(linelu[p].begin(), linelu[p].end(),
                    temp, [&](vector<int> ss, int tt) {
                    return ss < point[tt];
                }) - linelu[p].begin();
                if (l < r) {
                    if (l >= 1) pre = luSum[p][r - 1] - luSum[p][l - 1];
                    else pre = luSum[p][r - 1];
                }
            }
 
            p = lower_bound(lineVal.begin(), lineVal.end(),
                a - b) - lineVal.begin();
            if (p < lineVal.size() && lineVal[p] == a - b && !linerb[p].empty())
            {
                vector<int> temp = { (int)(a + 1), 0, 0 };
                int l = lower_bound(linerb[p].begin(), linerb[p].end(),
                    temp, [&](int tt, vector<int> ss) {
                    return point[tt] < ss;
                }) - linerb[p].begin();
                int r = upper_bound(linerb[p].begin(), linerb[p].end(), b - 1, [&](int bb, int tt) {
                    if (bb != point[tt][1]) return bb < point[tt][1];
                    else return false;
                }) - linerb[p].begin();
                if (l < r) nxt = rbSum2[p].qry(l, r) % mod;
            }
        }
        else {
            vector<int> temp = { q[1], q[2], 1987654321 };
            int pidx = lower_bound(point.begin(), point.end(), temp, [](vector<int> a, vector<int> b) {
                if (a[0] != b[0]) return a[0] < b[0];
                if (a[1] != b[1]) return a[1] > b[1];
                return a[2] > b[2];
            }) - point.begin();
            pre = dp[pidx] % mod; nxt = dp2[pidx] % mod;
        }
 
 
        long long nowans = answer.front();
        pre %= mod; nxt %= mod;
        if (type == 0) nowans += pre * nxt;
        else nowans -= pre * nxt;
        while (nowans < 0) { nowans += (2 + (-nowans) / mod) * mod; }
        nowans %= mod;
 
        answer.push_back(nowans);
    }
    return answer;
}


