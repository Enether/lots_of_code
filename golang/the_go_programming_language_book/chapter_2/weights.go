// weights.go converts pounds to kilograms and vice versa
package main

import (
	"os"
	"fmt"
	"strconv"
	"math"
)

const (
	KG_TO_LBS_RATE = 2.20462262185
	LBS_TO_KG_DIV_RATE = 0.45359237
)

type Kilogram int
type Pound int

func main() {
	var weightAmount int
	var weightType string

	if len(os.Args) < 3 {
		for {
			fmt.Println("Please enter the type of weight you'd like to convert (lbs/kg)")
			fmt.Scanf("%s\n", &weightType)
			if weightType != "lbs" && weightType != "kg" {
				fmt.Println("Invalid type!")
			} else {
				break
			}
		}
		fmt.Println("Please enter the amount of", weightType, "you'd like to convert:")
		fmt.Scanf("%d", &weightAmount)

		fmt.Println(weightType)
		fmt.Println(weightAmount)
	} else {
		weightType := os.Args[2]
		if weightType != "lbs" && weightType != "kg" {
			panic("Invalid weight type!")
		}
		var err error
		weightAmount, err = strconv.Atoi(os.Args[3])

		if err != nil {
			panic("Invalid integer amount!")
		}
	}

	if weightType == "lbs" {
		// lbs to kg
		fmt.Println(weightAmount, "pounds are equal to", Pound(weightAmount).ToKG(), "kilograms")
	} else {
		// kg to lbs
		fmt.Println(weightAmount, "kilograms are equal to", Kilogram(weightAmount).ToLBS(), "pounds")
	}
}

// ToLbs converts kilograms to pounds
func (kilogram Kilogram) ToLBS() Pound {
	return Pound(Round(float64(kilogram) * KG_TO_LBS_RATE, 0.01, 1))
}

// ToKG converts pounds to kilograms
func (pound Pound) ToKG() Kilogram {
	return Kilogram(Round(float64(pound) * LBS_TO_KG_DIV_RATE, 0.5, 0))
}


func Round(val float64, roundOn float64, places int ) (newVal float64) {
	var round float64
	pow := math.Pow(10, float64(places))
	digit := pow * val
	_, div := math.Modf(digit)
	if div >= roundOn {
		round = math.Ceil(digit)
	} else {
		round = math.Floor(digit)
	}
	newVal = round / pow
	fmt.Println(newVal)
	return
}