package main

import "fmt"

func main() {
	var N, i, j int
	fmt.Scan(&N)

	for i = 1; i <= N; i++ {
		for j = 1; j <= i; j++ {
			fmt.Print("*")
		}
		fmt.Println()
	}
}
