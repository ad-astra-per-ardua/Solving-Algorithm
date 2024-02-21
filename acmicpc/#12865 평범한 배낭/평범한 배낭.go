package main
import "fmt"
func main() {
	var n, k int
	fmt.Scan(&n, &k)
	put := make([][2]int, n+1)
	bag := make([][]int, n+1)

	for i := range bag {
		bag[i] = make([]int, k+1)
	}
	for i := 1; i <= n; i++ {
		fmt.Scan(&put[i][0], &put[i][1])
	}
	for i := 1; i <= n; i++ {
		for j := 1; j <= k; j++ {
			kg := put[i][0]
			val := put[i][1]
			if j < kg {
				bag[i][j] = bag[i-1][j]
			} else {
				bag[i][j] = max(val+bag[i-1][j-kg], bag[i-1][j])
			}
		}
	}
	fmt.Println(bag[n][k])
}
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
