#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int solution(int alp, int cop, vector<vector<int>> problems) {
    int max_alp_req = 0, max_cop_req = 0;

    for (auto problem : problems) {
        max_alp_req = max(max_alp_req, problem[0]);
        max_cop_req = max(max_cop_req, problem[1]);
    }
    
    vector<vector<int>> dp(max_alp_req + 1, vector<int>(max_cop_req + 1, INT_MAX));

    alp = min(alp, max_alp_req);
    cop = min(cop, max_cop_req);
    
    dp[alp][cop] = 0;
    
    for (int i = alp; i <= max_alp_req; ++i) {
        for (int j = cop; j <= max_cop_req; ++j) {
            if (i < max_alp_req)
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1);
            if (j < max_cop_req)
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1);
            
            for (auto problem : problems) {
                if (i >= problem[0] && j >= problem[1]) {
                    int new_alp = min(i + problem[2], max_alp_req);
                    int new_cop = min(j + problem[3], max_cop_req);
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[i][j] + problem[4]);
                }
            }
        }
    }

    return dp[max_alp_req][max_cop_req];
}
