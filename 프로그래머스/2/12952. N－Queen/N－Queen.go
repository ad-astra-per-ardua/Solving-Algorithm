package main

func solve2(row, col, ld, rd, n int, count *int) {
    if row == n {
        (*count)++
        return
    }

    pos := ((1 << n) - 1) &^ (col | ld | rd)
    for pos > 0 {
        p := pos & -pos
        pos -= p
        solve2(row+1, col|p, (ld|p)<<1, (rd|p)>>1, n, count)
    }
}

func solution(n int) int {
    count := 0
    solve2(0, 0, 0, 0, n, &count)
    return count
}
