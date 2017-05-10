package main

import (
	"fmt"
	"math"
)

func main() {
	matrixSize := 0
	matrix := [][]int{}

	readInteger(&matrixSize)
	//fmt.Println(matrixSize)
	readMatrix(&matrix, matrixSize)
	//fmt.Println(matrix)

	fmt.Println(math.Abs(float64(getDownLeftDiagSum(matrix, matrixSize)) - float64(getDownRightDiagSum(matrix, matrixSize))))
}

func getDownRightDiagSum(matrix [][]int, size int) int {
	var sum int
	for startR, startC := 0, 0; startR < size && startC < size; startR, startC = startR + 1, startC + 1{
		sum += matrix[startR][startC]
	}
	
	return sum
}
func getDownLeftDiagSum(matrix [][]int, size int) int {
	var sum int

	for startR, startC := 0, size-1; startR < size && startC >= 0; startR, startC = startR + 1, startC - 1{
		sum += matrix[startR][startC]
	}

	return sum
}

/*
Reads the matrix from the input
 */
func readMatrix(matrix *[][]int, size int) {
	// matrix is a pointer to a pointer, so we deref it
	// huh?
	for r := 0; r < size; r++ {
		*matrix = append(*matrix, make([]int, size))
		for c := 0; c < size; c++ {
			readInteger(&(*matrix)[r][c])
		}
	}
	//fmt.Println(matrix)
}

/*
Reads an integer from stdin
 */
func readInteger(integer *int) {
	_, err := fmt.Scanf("%d", integer)
	if err != nil {
		panic(err)
	}
}