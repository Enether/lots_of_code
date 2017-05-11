package main

import (
	"net"
)

type TicTacToe struct {
	board [][]string
	winner int
	playerOne net.Conn
	playerTwo net.Conn
	isPlayerOneTurn bool
}

func CreateGame(players []net.Conn) (TicTacToe, error) {
	if len(players) < 2 {
		panic("TANK")
	}
	tttGame := TicTacToe{
		board: createBoard(3, 3),
		playerOne: players[0],
		playerTwo: players[1],
		isPlayerOneTurn: true,
	}

	return tttGame, nil
}

func (ttt *TicTacToe) Move(x, y int) {
	var symbol string
	if ttt.isPlayerOneTurn {
		symbol = "[X]"
	} else {
		symbol = "[O]"
	}
	// TODO: Validate coords
	ttt.board[x][y] = symbol

	ttt.isPlayerOneTurn = !ttt.isPlayerOneTurn
}

/*
	Returns the player whose turn it is
 */
func (ttt *TicTacToe) GetActivePlayer() net.Conn {
	if ttt.isPlayerOneTurn {
		return ttt.playerOne
	}

	return ttt.playerTwo
}

func createBoard(xSize, ySize int) [][]string {
	board := make([][]string, xSize)
	for i := 0; i < xSize; i++ {
		board[i] = make([]string, ySize)
		for j := 0; j < ySize; j++ {
			board[i][j] = "[ ]"
		}
	}

	return board
}

//func main(){
//createBoard(3, 3)
//}
