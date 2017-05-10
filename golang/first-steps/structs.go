package main

import "fmt"

func main() {
	type courseMeta struct {
		Author string
		Level string
		Rating float64
	}

	//var GoFundamentals courseMeta
	//GoFundamentals := new(courseMeta)  # pointer
	goFundamentals := courseMeta{
		Author: "Tank",
		Level: "tank",
		Rating: 11.2,
	}

	fmt.Println(goFundamentals)
}
