package main

import (
	"fmt"
)

func brute_force(target int) int {
	sum := 0
	for i := 0; i < target; i++ {
		if i%3 == 0 || i%5 == 0 {
			sum += i
		}
	}
	return sum
}

func main() {
	var sum = brute_force(1000)
	fmt.Println(sum)
}
