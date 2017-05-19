package main

import (
	"crypto/sha256"
	"fmt"
)

func main() {
	firstSum := sha256.Sum256([]byte("tank"))
	secondSum := sha256.Sum256([]byte("traptraptraptraptraptrap"))

	differences := 0
	for idx := 0; idx < len(firstSum); idx++ {
		if firstSum[idx] != secondSum[idx] {
			differences++
		}
	}

	fmt.Println("There are", differences, "different bits in the hashes")
}
