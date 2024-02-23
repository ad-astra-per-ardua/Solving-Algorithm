function solution(a, b) {
    return a.reduce((acc, val, idx) => acc + val * b[idx], 0);
}