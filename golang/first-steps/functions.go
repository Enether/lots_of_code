package main

import (
	"fmt"
	"strings"
	"math"
)

func main () {
	module := "golang basics"
	author := "netherblood"

	fmt.Println(Converter(module, author))

	bestLeagueFinish := CalcBestLeagueFinishes(100, 12, 1, 3, 245)
	fmt.Println("Our best league finish was", bestLeagueFinish)
}

/* Converts the two strings to Title Case */
func Converter(mod, author string) (s1, s2 string) {
	return strings.Title(mod), strings.ToUpper(author)
}

/* Gets a variable number of int arguments and returns the best finish */
func CalcBestLeagueFinishes(finishes ...int) int {
	bestFinish := math.MaxInt32
	for finishIdx:= range finishes {
		finish := finishes[finishIdx]
		if finish < bestFinish {
			bestFinish = finish
		}
	}

	return bestFinish
}