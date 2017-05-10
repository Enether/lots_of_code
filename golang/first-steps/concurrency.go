package main

import (
	"time"
	"fmt"
	"sync"
)

var waitGrp sync.WaitGroup

func main() {
	waitGrp.Add(1)  // add the number of waitGrp goroutines
	asyncCalls()
	nonAsyncCalls()
	// program stops without awaiting our async sleep if we don't have this line below
	waitGrp.Wait()

	fmt.Println("\n\n\n\t\tCHANNELS DEMO\n\n\n")
	channels()
}

func asyncCalls() {
	go func() {
		defer waitGrp.Done()

		time.Sleep(3 * time.Second)
		fmt.Println("[ASYNC]  Sleeping like a b*tch")
	}()

	func() {
		fmt.Println("[ASYNC] At least I'm concurrent")
	}()

	//waitGrp.Wait()
}

func nonAsyncCalls() {
	func() {
		time.Sleep(3 * time.Second)
		fmt.Println("Sleeping like a b*tch")
	}()

	func() {
		fmt.Println("At least I'm concurrent")
	}()
}

func channels() {
	var waitChanns sync.WaitGroup
	waitChanns.Add(2)
	chnl := make(chan int)
	go func () {
		fmt.Println("1.[SENDER] Sent data ASYNC")
		go func() {defer waitChanns.Done(); chnl <- sleepSender()}()
		fmt.Println("1.[SENDER] Exiting out of sending")
	}()

	// This gets called first for some reason, maybe the waitgroup?
	go func() {
		defer waitChanns.Done()
		fmt.Println("3.[RECEIVER] Sleeping")
		time.Sleep(1 * time.Second)
		fmt.Println("3.[RECEIVER] Receiving")
		a := <-chnl
		fmt.Println("3.[RECEIVER]  Received", a)
	}()

	waitChanns.Wait()
}

func sleepSender() int {
	fmt.Println("2. [SLEEP SENDER]")
	time.Sleep(2 * time.Second)
	return 111
}