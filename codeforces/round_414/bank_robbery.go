package main

import "fmt"

func main() {
	var olegPos, leftGPos, rightGPos int
	readInteger(&olegPos)
	readInteger(&leftGPos)
	readIntegerNewLine(&rightGPos)
	var bankNoteCount int
	readIntegerNewLine(&bankNoteCount)
	var notes []int
	// read notes
	for i := 0; i < bankNoteCount; i++ {
		var num int
		readInteger(&num)
		notes = append(notes, num)
	}
	//bankNotes := make(map[int]int)
		var collectedNotes int

	for i := 0; i < bankNoteCount; i++ {
		num := notes[i]
		if num > leftGPos && num < rightGPos {
		  collectedNotes++
		}
		//bankNotes[num]++
	}
	//for i := olegPos-1; i >= 0 && i > leftGPos; i-- {
	//	collectedNotes += bankNotes[i]
	//}
	//collectedNotes += bankNotes[olegPos]
	//for i := olegPos+1; i < bankNoteCount && i < rightGPos; i++ {
	//	collectedNotes += bankNotes[i]
	//}

	fmt.Println(collectedNotes)
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

func readIntegerNewLine(integer *int) {
	_, err := fmt.Scanf("%d\n", integer)
	if err != nil {
		panic(err)
	}
}