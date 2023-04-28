#include <bits/stdc++.h>
using namespace std;

struct UF{
	int par[30303];
	UF(){
		for(int i=0; i<30303; i++) par[i] = i;
	}
	int find(int v){
		return v == par[v] ? v : par[v] = find(par[v]);
	}
	bool merge(int u, int v){
		u = find(u), v = find(v);
		if(u == v) return 0;
		par[u] = v;
		return 1;
	}
};

struct Seg{
	int tree[1 << 18];
	int bias = 1 << 17;

	void update(int x, int v){
		x |= bias; tree[x] = v;
		while(x >>= 1){
			tree[x] = tree[x << 1] + tree[x << 1 | 1];
		}
	}

	int query(int l, int r){
		l |= bias, r |= bias;
		int ret = 0;
		while(l <= r){
			if(l & 1) ret += tree[l++];
			if(~r & 1) ret += tree[r--];
			l >>= 1, r >>= 1;
		}
		return ret;
	}
}seg;

vector<int> inp[30303], g[30303];
int par[30303], sz[30303], top[30303], dep[30303], in[30303];
int arr[30303], chk[30303];
int pv;
int n, q;

void dfs(int v = 1){
	chk[v] = 1;
	for(auto i : inp[v]){
		if(chk[i]) continue;
		chk[i] = 1;
		g[v].push_back(i);
		dfs(i);
	}
}

void dfs1(int v = 1){
	for(auto &i : g[v]){
		par[i] = v;
		dep[i] = dep[v] + 1;
		dfs1(i);
		sz[v] += sz[i];
		if(sz[i] > sz[g[v][0]]) swap(i, g[v][0]);
	}
}

void dfs2(int v = 1){
	in[v] = ++pv;
	for(auto &i : g[v]){
		top[i] = i == g[v][0] ? top[v] : i;
		dfs2(i);
	}
}

void update(int x, int v){
	seg.update(in[x], v);
}

int query(int a, int b){
	int ret = 0;
	while(top[a] != top[b]){
		if(dep[top[a]] < dep[top[b]]) swap(a, b);
		int st = top[a];
		ret += seg.query(in[st], in[a]);
		a = par[st];
	}
	if(dep[a] > dep[b]) swap(a, b);
	ret += seg.query(in[a], in[b]);
	return ret;
}

struct Query{
	string op; int a, b;
};
vector<Query> qry;

int main(){
	top[1] = dep[1] = 1;
	ios_base::sync_with_stdio(0); cin.tie(0);
	UF uf;
	cin >> n;
	for(int i=1; i<=n; i++) cin >> arr[i];

	cin >> q;

	while(q--){
		string op; int a, b; cin >> op >> a >> b;
		qry.push_back({op, a, b});
		if(op == "bridge"){
			if(uf.merge(a, b)) inp[a].push_back(b), inp[b].push_back(a);
		}
	}
	for(int i=1; i<=n; i++){
		if(uf.merge(1, i)){
			inp[1].push_back(i); inp[i].push_back(1);
		}
	}

	dfs(); dfs1(); dfs2();
	for(int i=1; i<=n; i++) update(i, arr[i]);
	for(int i=0; i<30303; i++) uf.par[i] = i;

	for(auto i : qry){
		if(i.op == "bridge"){
			if(uf.merge(i.a, i.b)) cout << "yes\n";
			else cout << "no\n";
		}else if(i.op == "penguins"){
			update(i.a, i.b);
		}else{
			if(uf.find(i.a) != uf.find(i.b)) cout << "impossible\n";
			else cout << query(i.a, i.b) << "\n";
		}
	}
}
