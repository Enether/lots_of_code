package comma

import (
	"bytes"
)

// 1.1 Write a non-recursive version which uses Buffer
// comma inserts commas in a non-negative decimal integer string.
//func comma(s string) string {
//    n := len(s)
//    if n <= 3 {
//        return s
//    }
//    return comma(s[:n-3]) + "," + s[n-3:]
//}

func comma(s string) string {
	var buff bytes.Buffer
	stringLen := len(s)
	hasSign := false
	if s[0] == '-' || s[0] == '+' {
		stringLen -= 1  // so that modulo operations ignore the sign
		hasSign = true
	}

	if stringLen <= 3 {
		return s  // only three numbers, no use
	}

	// determine the first comma index
	firstIdx := stringLen % 3
	if firstIdx == 0 {  // normal comma spacing between three numbers
		firstIdx = 3
	}

	if hasSign {
		firstIdx++
	}

	buff.WriteString(s[:firstIdx])
	buff.WriteByte(',')

	// add numbers and commas until we reach the end
	commaIdx := firstIdx + 3
	lastCommaIdx := firstIdx
	for commaIdx < len(s) {
		buff.WriteString(s[lastCommaIdx:commaIdx])
		buff.WriteByte(',')

		lastCommaIdx = commaIdx
		commaIdx += 3
	}

	buff.WriteString(s[lastCommaIdx:])

	return buff.String()
}

