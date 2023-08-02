#include <string>
#include <vector>
#include <cstring>
#include <algorithm>
 
using namespace std;
int arr[110][110];
vector<pair<int, int> > pos['Z' + 5];
 
bool able(char ch)
{
    if(pos[ch].empty()) return false;
    int x = pos[ch][0].first;
    int y = pos[ch][0].second;
    int nx = pos[ch][1].first;
    int ny = pos[ch][1].second;
    int a = x, b = y;
    bool flag = true;
    while(flag && a != nx){
        if(a > nx) a--;
        else if(a < nx) a++;
        if(a != nx || b != ny){
            if(arr[a][b] != '.') flag = false;
        }
    }
    while(flag && b != ny){
        if(b > ny) b--;
        else if(b < ny) b++;
        if(a != nx || b != ny){
            if(arr[a][b] != '.') flag = false;
        }
    }
    if(flag) return true;
    flag = true; a = x; b = y;
    while(flag && b != ny){
        if(b > ny) b--;
        else if(b < ny) b++;
        if(a != nx || b != ny){
            if(arr[a][b] != '.') flag = false;
        }
    }
    while(flag && a != nx){
        if(a > nx) a--;
        else if(a < nx) a++;
        if(a != nx || b != ny){
            if(arr[a][b] != '.') flag = false;
        }
    }
    if(flag) return true;
    return false;
}
 
string solution(int m, int n, vector<string> board) {
    for(int i=0;i<'Z'+5;i++) pos[i].clear();
    memset(arr, -1, sizeof(arr));
    for(int i=0;i<m;i++)
    {
        for(int j=0;j<n;j++)
        {
            arr[i][j] = board[i][j];
            if('A' <= arr[i][j] && arr[i][j] <= 'Z'){
                pos[arr[i][j]].push_back(make_pair(i, j));
            }
        }
    }
    bool flag = true;
    string answer = "";
    while(flag)
    {
        flag = false;
        for(int i='A';i<='Z';i++){
            flag = able(i);
            if(flag) {
                arr[pos[i][0].first][pos[i][0].second] = '.';
                arr[pos[i][1].first][pos[i][1].second] = '.';
                pos[i].clear();
                answer += i; break;
            }
        }
    }
    
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            if(arr[i][j] != '.' && arr[i][j] != '*') return "IMPOSSIBLE";
        }        
    }
  
    return answer;
}