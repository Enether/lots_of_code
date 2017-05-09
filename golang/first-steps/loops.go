package main

import (
	"fmt"
	"time"
)

func main() {
	// infinite loop
	//for {
	//
	//}
	i := 1
	for i < 10 {
		i++
	}

	for j := 0; j < getMaxLoopVal(); j++ {

	}

	for timer := 10; timer >= 0; timer-- {
		if timer == 0 {
			fmt.Println("BOOM")
			break
		} else if timer % 2 == 0 {
			continue
		}
		time.Sleep(time.Duration(0.3 * float64(time.Second)))
		fmt.Println(timer)
	}

	coursesInProg := []string{"Ruby Fundamentals", "Go", "Rust", "Python"}
	coursesCompleted := []string{"Ruby Fundamentals", "Go", "Rust", "Python"}
	// O(N^2) :O
	for idx, course := range coursesInProg {
		fmt.Println("Course at", idx, "is", course)
		completedCoursesCount := 0
		for _, completedCourse := range coursesCompleted {
			if completedCourse == course {
				break
			}
			completedCoursesCount++
		}
		fmt.Println("Completed", completedCoursesCount, "courses")
	}

	fmt.Println("This complexity is too high!")
	for i := 0; i < 100000; i++ {
		asymptoticPoint:
		for j := 0; j < 100000; j++ {
			for k := 0; k < 100000; k++ {
				for l := 0; l < 100000; l++ {
					for m := 0; m < 100000; m++ {
						break asymptoticPoint
					}
				}
			}
		}
	}
	fmt.Println("NO FEAR! We have break labels")

}

func getMaxLoopVal() int {
	fmt.Println("called getMaxLoopVal()")
	return 5
}
