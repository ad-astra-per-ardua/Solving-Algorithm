const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, K] = input[0].split(' ').map(Number);
const items = input.slice(1).map(line => line.split(' ').map(Number));

const dp = Array.from(Array(N + 1), () => Array(K + 1).fill(0));

for (let i = 1; i <= N; i++) {
    const [weight, value] = items[i - 1];

    for (let j = 1; j <= K; j++) {
        if (j < weight) {
            dp[i][j] = dp[i - 1][j];
        } else {
            dp[i][j] = Math.max(value + dp[i - 1][j - weight], dp[i - 1][j]);
        }
    }
}

console.log(dp[N][K]);
