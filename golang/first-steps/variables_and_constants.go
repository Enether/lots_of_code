package main

import (
	"fmt"
	"reflect"
	"os"
)

var (
	name, course string
	module float64
	infer = "Tank"
)

func main() {
	fmt.Println("Name is [", name, "] and is of type", reflect.TypeOf(name))
	fmt.Println("Module is", module, " and is of type", reflect.TypeOf(module))
	fmt.Println("It can also infer types - ", infer, reflect.TypeOf(infer))

	a := 10.123
	b := 10

	// c := a + b  will throw
	c := int(a) + b
	fmt.Println("Combined a and b to get c:", c, reflect.TypeOf(c))

	// POINTERS!
	what := "31431"
	ptr := &what

	fmt.Println("Well looky here, something at", ptr, "is equal to", *ptr)

	curr_course := "golang programming"
	fmt.Println("\nCurrently at course", curr_course)
	changeCourse(&curr_course)
	fmt.Println("Now at course", curr_course)

	// Env variables
	for _, env := range os.Environ() /* list of env variables */{
		fmt.Println("Env var: ", env)
		break
	}

	fmt.Println("Our home is", os.Getenv("HOME"))
}

func changeCourse(course *string) string {
	*course = "tank"

	return *course
}