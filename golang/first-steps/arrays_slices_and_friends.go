package main

import "fmt"

func main() {
	// slice of 5 ""
	myCourses := make([]string, 5, 10)
	fmt.Println(myCourses[0])

	myCoursesInitializedBetter := []string{"Tank", "Tank", "tank"}
	fmt.Println(myCoursesInitializedBetter[1])

	fmt.Println(myCoursesInitializedBetter)
	sliceOfSlice := myCoursesInitializedBetter[0:1]  // just like python <3
	fmt.Println(sliceOfSlice)

	// let's prove that it doubles the internal array
	smallSlice := make([]int, 1, 2)  // 2 capacity!
	fmt.Println("Capacity is", cap(smallSlice))
	for i := 0; i < 10; i++ {
		smallSlice = append(smallSlice, 10)
	}
	fmt.Println("Capacity is", cap(smallSlice))

	firstSlice := []int {1, 2, 3}
	secondSlice := []int {4, 5, 6}
	fmt.Println("\n\nCombined slices", append(firstSlice, secondSlice...))
}
