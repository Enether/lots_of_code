package main

import "fmt"

func main() {
	var gradeCount, currGrade int
	readInteger(&gradeCount)
	for i := 0; i < gradeCount; i++ {
		readInteger(&currGrade)
		if currGrade > 37 {
			currGrade = roundToCloseFiveMultiple(currGrade, 3)
		}
		fmt.Println(currGrade)
	}
}

/*
Tries to round an integer to a multiple of five that is a less than 3 numbers away
 */
func roundToCloseFiveMultiple(number, maxDiff int) (i int) {
	for i = number; i < number+maxDiff; i++  {
		if i % 5 == 0 {
			return i
		}
	}
	return number
}


/*
Reads an integer from stdin
 */
//noinspection ALL
func readInteger(integer *int) {
	_, err := fmt.Scanf("%d", integer)
	if err != nil {
		panic(err)
	}
}