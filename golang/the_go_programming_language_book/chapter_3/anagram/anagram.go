package anagram

import (
	"reflect"
	"unicode"
)

func AreAnagrams(word1, word2 string) (areAnagrams bool) {
	firstWordLetters := make(map[rune]int)
	for _, chr := range word1 {
		if unicode.IsLetter(chr) {
			firstWordLetters[unicode.ToLower(chr)]++
		}
	}

	secondWordLetters := make(map[rune]int)
	for _, chr := range word2 {
		if unicode.IsLetter(chr) {
			secondWordLetters[unicode.ToLower(chr)]++
		}
	}

	return reflect.DeepEqual(firstWordLetters, secondWordLetters)
}
