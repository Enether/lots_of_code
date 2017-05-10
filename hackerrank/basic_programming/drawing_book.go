package main

import (
	"fmt"
	"math"
)

func main() {
	var pageCount, wantedPage int
	readInteger(&pageCount)
	readInteger(&wantedPage)

	pagesToTurn := math.Min(float64(wantedPage), float64(pageCount - wantedPage))

	if pageCount != 2 && pageCount % 2 == 0 && wantedPage == pageCount - 1 {
		// even number of pages and we want the next to last page
		// 6, 5 - pages 1/2, 3/4, 5/6. 5 is on the frontside, so if we start from 6 we have to turn to it
		pagesToTurn++
	}
	fmt.Println(int32(pagesToTurn/2))
}

/*
Reads an integer from stdin
 */
func readInteger(integer *int) {
	_, err := fmt.Scanf("%d", integer)
	if err != nil {
		panic(err)
	}
}