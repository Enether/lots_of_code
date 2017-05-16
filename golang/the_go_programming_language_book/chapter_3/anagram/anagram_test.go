package anagram

import (
	"testing"
	"fmt"
)

func TestAnagram(t *testing.T) {
	words := [][]string{ {"tank", "knat"}, {"listen", "silent"}, {"Mother-in-law", "Hitler woman"}, {"debit card", "Bad CreDiT"}, {"bg", "gbb"}, {"maina", "aina"}}
	expectedResults := []bool { true, true, true, true, false, false}

	for idx, wordPair := range words {
		expectedResult := expectedResults[idx]
		receivedResult := AreAnagrams(wordPair[0], wordPair[1])

		if receivedResult != expectedResult {
			if expectedResult {
				fmt.Printf("%s and %s are anagrams but the function returned false!\n\n", wordPair[0], wordPair[1])
			} else {
				fmt.Printf("%s and %s are not anagrams but the function returned true!\n\n", wordPair[0], wordPair[1])
			}
			t.Fail()
		}
	}
}
