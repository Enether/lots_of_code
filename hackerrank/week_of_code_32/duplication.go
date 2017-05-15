package main

import (
	"fmt"
	"strconv"
	"math"
)

var (
	mainStr = "01"
	str = "10"
)

func init() {
	// Pre-compute the big string
	for len(mainStr) < 1200 {
		mainStr += str
		str = getStr(mainStr)
	}
}

func main() {
	var queryCount int
	fmt.Scanf("%d\n", &queryCount)
	for i := 0; i < queryCount; i++ {
		var wantedIdx int
		fmt.Scanf("%d\n", &wantedIdx)
		fmt.Println(string(mainStr[wantedIdx]))
	}
}

func getStr(m string) string {
	newStr := ""
	for i := 0; i < len(m); i++ {
		parsedNum, _ := strconv.Atoi(string(m[i]))
		newStr += strconv.Itoa(int(math.Abs(float64(1 - parsedNum))))
	}
	return newStr
}
