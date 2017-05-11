package main

import "fmt"

const searchedLetter = 'a'

func main() {
	var givenWord string
	_, err := fmt.Scan(&givenWord)
	if err != nil {
		panic("WTF")
	}

	var endIndex int
	_, scanfErr := fmt.Scanf("%d", &endIndex)
	if scanfErr != nil {
		panic("WTF")
	}

	wordLen := len(givenWord)

	letterCount := 0
	if wordLen <= endIndex {
		// add the times the word is repeated
		letterCount += getLetterCountInWord(givenWord, wordLen) * (endIndex/wordLen)
	}
	leftOverCount := getLetterCountInWord(givenWord, endIndex % wordLen)  // get any left over part we've missed from above
	fmt.Println(letterCount + leftOverCount)
}

func getLetterCountInWord(word string, endIdx int) (letterCount int) {
	for i := 0; i < endIdx; i++ {
		if word[i] == searchedLetter {
			letterCount++
		}
	}

	return letterCount
}