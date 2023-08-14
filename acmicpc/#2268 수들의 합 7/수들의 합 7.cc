#include <iostream>
#include <vector>
using namespace std;

vector<long long> tree;

void Modify(int node, int start, int end, int index, long long value) {
    if (index < start || index > end) return;
    
    if (start == end) {
        tree[node] = value;
        return;
    }

    Modify(node*2, start, (start+end)/2, index, value);
    Modify(node*2+1, (start+end)/2 + 1, end, index, value);
    tree[node] = tree[node*2] + tree[node*2+1];
}

long long Sum(int node, int start, int end, int left, int right) {
    if (left > end || right < start) return 0;

    if (left <= start && right >= end) return tree[node];

    return Sum(node*2, start, (start+end)/2, left, right) + Sum(node*2+1, (start+end)/2 + 1, end, left, right);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    cin >> N >> M;

    tree.resize(4*N, 0);
    vector<long long> L(N, 0);
    for (int i = 0; i < M; i++) {
        int Q, A;
        long long B;
        cin >> Q >> A >> B;

        if (Q == 0) {
            if (A > B) {
            int temp = A;
            A = B;
            B = temp;
                
            }
            cout << Sum(1, 0, N-1, A-1, B-1) << '\n';
        } else {
            Modify(1, 0, N-1, A-1, B);
        }
    }

    return 0;
}
