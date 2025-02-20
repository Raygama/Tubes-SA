package main

import "fmt"

func main() {
	var X, oddCount, evenCount, digit int

	fmt.Scan(&X)

	oddCount = 0
	evenCount = 0

	for X > 0 {
		digit = X % 10
		if digit%2 == 0 {
			evenCount++
		} else {
			oddCount++
		}
		X /= 10
	}

	fmt.Println(oddCount, evenCount)
}
