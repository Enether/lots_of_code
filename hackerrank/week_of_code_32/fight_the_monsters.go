package main

import (
	"fmt"
	"sort"
)


func main() {
	var monsterCount, hitDamage, seconds, killedMonsters int
	fmt.Scanf("%d %d %d", &monsterCount, &hitDamage, &seconds)
	monsters, _ := intScanln(monsterCount)
	sort.Ints(monsters)
	//fmt.Println(monsters)

	for _, monster := range monsters {
		// figure out the amount of hits we need
		neededHits := monster / hitDamage

		if monster % hitDamage != 0 {
			// we need one more hit
			neededHits++
		}

		seconds -= neededHits
		if seconds >= 0 {
			// this was a valid kill and we have seconds to go
			killedMonsters++
		} else {
			break
		}
	}

	fmt.Println(killedMonsters)

}

/*
	Read an array of integers
 */
func intScanln(n int) ([]int, error) {
    x := make([]int, n)
    y := make([]interface{}, len(x))

	// Make everything in y a reference to x
    for i := range x {
        y[i] = &x[i]
    }
	// Fill y
    n, err := fmt.Scanln(y...)
    x = x[:n]
    return x, err
}