#include<bits/stdc++.h>
using namespace std;

vector<int> inorder, postorder, position;
int n;

void preorder(int in_start, int in_end, int post_start, int post_end) {
    if(in_start > in_end || post_start > post_end) return;
    
    int parents = postorder[post_end];
    cout << parents << " ";

    int left = position[parents] - in_start;
    int right = in_end - position[parents];

    preorder(in_start, in_start + left - 1, post_start, post_start + left - 1); 
    preorder(in_end - right + 1, in_end, post_end - right, post_end - 1); 
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    inorder.resize(n); 
    postorder.resize(n);
    position.resize(n + 1);

    for(int i = 0; i < n; i++) cin >> inorder[i];
    for(int i = 0; i < n; i++) cin >> postorder[i];
    for(int i = 0; i < n; i++) position[inorder[i]] = i;

    preorder(0, n - 1, 0, n - 1);
    return 0;
}
