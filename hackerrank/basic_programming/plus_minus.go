package main

import "fmt"

// https://www.hackerrank.com/challenges/plus-minus
func main() {
    var (
		numCount, negativeNums, positiveNums, zeroNums int
	)
    _, err := fmt.Scanf("%d", &numCount)
	if err != nil {
		panic("tank")
	}

	for i := 0; i < numCount; i++ {
		var currNum int
		_, err := fmt.Scanf("%d", &currNum)
		if err != nil {
			panic("tank")
		}

		if currNum < 0 {
			negativeNums++
		} else if currNum > 0 {
			positiveNums++
		} else {
			zeroNums++
		}
	}
	fmt.Printf("%.6f\n", divideIntegers(positiveNums, numCount))
	fmt.Printf("%.6f\n", divideIntegers(negativeNums, numCount))
	fmt.Printf("%.6f\n", divideIntegers(zeroNums, numCount))
}

func divideIntegers(a, b int) float64 {
	return float64(a) / float64(b)
}