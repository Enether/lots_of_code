package comma

import (
	"testing"
	"fmt"
)

func TestComma(t *testing.T) {
	words := []string{"123456", "12345", "1234", "123", "-123", "-12345678912314", "-123413.12", "-22123413.12", "-1.2", "-123.2"}
	expectedWords := []string{"123,456", "12,345", "1,234", "123", "-123", "-12,345,678,912,314", "-123,413.12", "-22,123,413.12", "-1.2", "-123.2"}

	for idx := range words {
		expectedWord := expectedWords[idx]
		receivedWord := comma(words[idx])

		if expectedWord != receivedWord {
			fmt.Printf("ERROR: Expected %s but received %s from the string %s\n\n", expectedWord, receivedWord, words[idx])
			t.Fail()
		}
	}
}

func TestFindFloatingPoint(t *testing.T) {
	words := []string{"123.456", "1.2345", "12.34", "12.3", "-1.23", "-1234567891.2314"}
	expectedFloatingPointIndices := []int{3, 1, 2, 2, 2, 11}

	for idx := range words {
		expectedIdx := expectedFloatingPointIndices[idx]
		receivedIdx, _ := findFloatingPoint(words[idx])

		if expectedIdx != receivedIdx {
			fmt.Printf("ERROR: Expected the number %s to have a floating point at index: %d but received index: %d\n\n", words[idx], expectedIdx, receivedIdx)
			t.Fail()
		}
	}
}