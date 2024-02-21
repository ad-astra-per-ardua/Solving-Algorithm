import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[][] put = new int[n + 1][2];
        int[][] bag = new int[n + 1][k + 1];

        for (int i = 1; i <= n; ++i) {
            st = new StringTokenizer(br.readLine());
            put[i][0] = Integer.parseInt(st.nextToken());
            put[i][1] = Integer.parseInt(st.nextToken());
        }

        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= k; ++j) {
                int kg = put[i][0];
                int val = put[i][1];

                if (j < kg) {
                    bag[i][j] = bag[i - 1][j];
                } else {
                    bag[i][j] = Math.max(val + bag[i - 1][j - kg], bag[i - 1][j]);
                }
            }
        }

        System.out.println(bag[n][k]);
    }
}
