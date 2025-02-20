package main

import "fmt"

func main() {
	var N, count, a, b, temp int

	fmt.Scan(&N)
	count = 0
	a = 1
	b = 1

	for count < N {
		if a%2 != 0 {
			fmt.Print(a, " ")
			count++
		}
		temp = a + b
		a = b
		b = temp
	}
	fmt.Println()
}
