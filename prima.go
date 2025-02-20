package main

import "fmt"

func main() {
	var num, i int
	var isPrime bool
	fmt.Scan(&num)

	isPrime = num > 1
	for i = 2; i*i <= num; i++ {
		isPrime = isPrime && (num%i != 0)
	}

	if isPrime {
		fmt.Println("Prima")
		// fmt.Println("Prime")
	} else {
		fmt.Println("Bukan Prima")
		// fmt.Println("Not Prime")
	}
}
