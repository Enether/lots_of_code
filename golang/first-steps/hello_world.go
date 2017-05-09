package main

import (
	"fmt"
	"runtime"
)

func main () {
	fmt.Println("Hello, Gopher!")
	fmt.Println("Calling from ", runtime.GOOS, runtime.Version(), runtime.GOROOT())
}
