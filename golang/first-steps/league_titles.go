package main

import (
	"fmt"
)

func main() {
	leagueTitles := make(map[string]int)
	leagueTitles["Bayern Munchen"] = 23
	leagueTitles["Borussia Dortmund"] = 23

	futureLeagueTitles := map[string]int {
		"Red Bull Leipzig": 1000,
		"McGladbah": 1,
	}

	fmt.Println(leagueTitles)
	fmt.Println(futureLeagueTitles)

	testOrdering := make(map[int]bool)
	for i := 0; i < 100; i++ {
		testOrdering[i] = true
	}

	fmt.Println(testOrdering)  // non ordered

	testIterating := map[string]int {
		"hello": 1,
		"whatsup": 2,
		"notuch": 3,
	}

	for msg, count := range testIterating {
		fmt.Println(msg, count)
	}

	testIterating["new message for the pessage"] = 100
	fmt.Println(testIterating["new message for the pessage"])
	delete(testIterating, "new message for the pessage")
	fmt.Println(testIterating["new message for the pessage"])  // will print out 0
	fmt.Println(testIterating["NON EXISTANT"])  // will print out 0
	delete(testIterating, "NON EXISTANT")

}
