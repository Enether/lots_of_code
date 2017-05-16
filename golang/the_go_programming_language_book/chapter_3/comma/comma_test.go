package comma

import (
	"testing"
	"fmt"
)

func TestComma(t *testing.T) {
	words := []string{"123456", "12345", "1234", "123", "-123", "-12345678912314"}
	expectedWords := []string{"123,456", "12,345", "1,234", "123", "-123", "-12,345,678,912,314"}

	for idx := range words {
		expectedWord := expectedWords[idx]
		receivedWord := comma(words[idx])

		if expectedWord != receivedWord {
			fmt.Printf("ERROR: Expected %s but received %s from the string %s\n\n", expectedWord, receivedWord, words[idx])
			t.Fail()
		}
	}
}
