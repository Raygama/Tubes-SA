package main

import "fmt"

func main() {
	var N, reversed, temp int

	fmt.Scan(&N)
	temp = N
	reversed = 0

	for temp > 0 {
		reversed = reversed*10 + temp%10
		temp /= 10
	}

	if N == reversed {
		fmt.Println("Palindrom")
		// fmt.Println("Not Palindrome")
	} else {
		fmt.Println("Bukan Palindrom")
		// mt.Println("Not Palindrome")
	}
}
