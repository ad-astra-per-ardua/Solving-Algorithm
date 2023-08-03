#include<bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int num_problem, num_compare;
    cin >> num_problem >> num_compare;

    vector<int> problem_list[num_problem+1];
    int indegree[num_problem+1];
    priority_queue<int, vector<int>, greater<int>> heap;
    vector<int> result;

    fill_n(indegree, num_problem+1, 0);

    for(int i = 0; i < num_compare; i++) {
        int A, B;
        cin >> A >> B;
        problem_list[A].push_back(B);
        indegree[B]++;
    }

    for(int i = 1; i <= num_problem; i++) {
        if(indegree[i] == 0) {
            heap.push(i);
        }
    }

    while(!heap.empty()) {
        int temp = heap.top();
        heap.pop();
        result.push_back(temp);
        for(int j: problem_list[temp]) {
            indegree[j]--;
            if(indegree[j] == 0) {
                heap.push(j);
            }
        }
    }

    for(int i: result) {
        cout << i << " ";
    }

    return 0;
}
