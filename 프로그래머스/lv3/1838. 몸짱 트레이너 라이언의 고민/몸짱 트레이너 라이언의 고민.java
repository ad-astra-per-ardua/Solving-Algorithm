import java.util.*;
import java.lang.Math;

public class Solution {
    private int[][] arr = new int[110][110];

    private int foo2(int n, int gap) {
        int res = 0;
        while (true) {
            int x = 0, y = 0;
            boolean flag = true;
            for (int j = 0; flag && j < n; j++) {
                for (int i = 0; flag && i < n; i++) {
                    if (arr[i][j] == 0) {
                        res++;
                        x = i;
                        y = j;
                        flag = false;
                        break;
                    }
                }
            }
            if (!flag) {
                arr[x][y] = 2;
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < n; j++) {
                        if (arr[i][j] == 0 && Math.abs(i - x) + Math.abs(j - y) <= gap) arr[i][j] = 1;
                    }
                }
            } else break;
        }
        return res;
    }

    private int foo(int n, int gap) {
        int res = 0;
        for(int j=0;j<n;j++){
            for(int[] row: arr)
                Arrays.fill(row, 0);
            arr[0][j] = 2;
            for(int a=0;a<n;a++)
                for(int b=0;b<n;b++)
                    if(Math.abs(a)+Math.abs(b-j)<=gap) arr[a][b] = 1;
            res = Math.max(res, foo2(n, gap) + 1);
        }
        return res;
    }

    public int solution(int n, int m, int[][] timetable) {
        int answer = 0;
        int[] mark = new int[1330];
        Arrays.fill(mark, 0);
        for(int[] v : timetable) {
            mark[v[0]]++;
            mark[v[1]+1]--;
        }
        int with = 0, now = 0;
        for(int i=0;i<mark.length;i++){
            now += mark[i];
            with = Math.max(with, now);
        }
        if(with <= 1) return 0;
        int[] gap = new int[30];
        for(int i=0;i<30;i++) gap[i] = foo(n, i);
        answer = 0;
        while(gap[answer] >= with) answer++;
        return answer;
    }
}
