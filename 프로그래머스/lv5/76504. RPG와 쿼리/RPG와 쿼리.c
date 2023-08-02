#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#define MAX_N 3000
#define MAX_P 2501
#define MAX_Q 100000

int weight[MAX_N][MAX_N];
int reverseRoad[MAX_N][MAX_N];
int reverseRoadSize[MAX_N];

long long turnsForAmount[MAX_N][MAX_P], minTurns[MAX_P];

void minimize(long long *x, long long y){
    if(*x == -1 || *x > y) 
        *x = y; 
}

long long* solution(int n, int z, int** roads, size_t roads_rows, size_t roads_cols, long long* queries, size_t queries_len) {
    memset(reverseRoad, 0, sizeof(reverseRoad));
    memset(reverseRoadSize, 0, sizeof(reverseRoadSize));
    memset(minTurns, -1, sizeof(minTurns));
    memset(turnsForAmount, -1, sizeof(turnsForAmount));

    for(int i = 0; i < roads_rows; ++i){
        int* road = roads[i];
        reverseRoad[road[1]][reverseRoadSize[road[1]]++] = road[0];
        weight[road[0]][road[1]] = road[2];
    }

    minTurns[0] = turnsForAmount[0][0] = 0;
    
    for(int i = 1; i < n; ++i) 
        turnsForAmount[i][0] = 1;
    
    for(int p = 1; p < MAX_P; ++p){
        for(int i = 0; i < n; ++i)
            for(int j = 0; j < reverseRoadSize[i]; ++j){
                int from = reverseRoad[i][j];
                if(p - weight[from][i] >= 0 && turnsForAmount[from][p - weight[from][i]] != -1)
                    minimize(&turnsForAmount[i][p], turnsForAmount[from][p - weight[from][i]] + 1);
            }

        if(p >= z && minTurns[p-z] != -1)
            minimize(&minTurns[p], minTurns[p-z] + 1);
        
        for(int i = 0; i < n; ++i)
            if(turnsForAmount[i][p] != -1) 
                minimize(&minTurns[p], turnsForAmount[i][p]);
        
        for(int i = 0; i < n; ++i)
            if(minTurns[p] != -1) 
                minimize(&turnsForAmount[i][p], minTurns[p] + 1);
    }

    long long* answer = (long long*)malloc(sizeof(long long) * queries_len);
    
    for(int i = 0; i < queries_len; ++i){
        long long q = queries[i];
        long long ans = -1;
        if(q < MAX_P) 
            ans = minTurns[q];
        else{
            long long i = MAX_P - 1;
            for(;i != -1; --i) 
                if(i % z == q % z) 
                    break;
            
            if(minTurns[i] != -1) 
                ans = (q-i) / z + minTurns[i];
        }
        answer[i] = ans;
    }
    return answer;
}
