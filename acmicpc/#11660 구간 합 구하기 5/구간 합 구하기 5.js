const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const [N, M] = input[0].split(' ').map(Number);
let board = Array.from(Array(N+1), () => Array(N+1).fill(0));
let sum = Array.from(Array(N+1), () => Array(N+1).fill(0));

for(let i=1; i<=N; i++){
    let row = input[i].split(' ').map(Number);
    for(let j=1; j<=N; j++){
        board[i][j] = row[j-1];
    }
}

for(let i=1; i<=N; i++){
    for(let j=1; j<=N; j++){
        sum[i][j] = sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1] + board[i][j];
    }
}

let answer = '';
for(let i=0; i<M; i++){
    const [x1, y1, x2, y2] = input[N+1+i].split(' ').map(Number);
    answer += (sum[x2][y2] - sum[x1-1][y2] - sum[x2][y1-1] + sum[x1-1][y1-1]) + '\n';
}
console.log(answer.trim());
