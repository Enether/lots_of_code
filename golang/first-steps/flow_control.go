package main
import (
	"fmt"
	"math/rand"
	"time"
	"os"
)
func main () {
	//firstCourseRank := 41
	//secondCourseRank := 2000

	if firstCourseRank, secondCourseRank := 41, 2000; /*best thing ever*/firstCourseRank < secondCourseRank {
		fmt.Println("First course is doing better than the second course")
	} else if secondCourseRank > firstCourseRank {
		fmt.Println("Second course isn't doing that well")
	} else {
		fmt.Println("Courses are doing equally well")
		fmt.Println("Or something weird is going on")
	}

	_, err := os.Open("open_smth.txt")
	if err != nil {
		fmt.Println("Error while opening!", err)
	}

	// fmt.Println(firstCourseRank) - throws

	switch "logic301" {
		case "logic301":
			fmt.Println("Keeping it G")
		// no fallthrough by default
		case "cause now I know I've got it":
			fmt.Println("Nice man")
		case "that's why Uber has signed me on the dotted":
			fmt.Println("Sure hope so")
		default:
			fmt.Println("oh well")
	}

	// fallthrough example
	switch "tank" {
		case "tank":
			fmt.Println("tnk")
			fallthrough
		case "not Tank":
			fmt.Println("Still tank")
		default:
			fmt.Println("WTF")
	}

	switch randNum := getRandNum(); randNum {
		case 0, 2, 4, 6, 8, 10:
			fmt.Println("EVEN NUMBER", randNum)
		case 1, 3, 5, 7:
			fmt.Println("ODD NUMBER", randNum)
		default:
			fmt.Println("NINE", randNum)
	}

}

func getRandNum() int {
	timeSeed := time.Now().Unix()
	rand.Seed(timeSeed)

	return rand.Intn(10)
}