#include <string>
#include <vector>
#include <numeric>

using namespace std;

int solution(vector<int> a, vector<int> b) {
    return std::inner_product(a.begin(), a.end(), b.begin(), 0);
}