func solution(a []int, b []int) int {
    var result int
    for i, v := range a {
        result += v * b[i]
    }
    return result
}