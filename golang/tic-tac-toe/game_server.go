package main

import (
	"net"
	"fmt"
	"log"
	"strconv"
)

func RunGame(players []net.Conn) error {
	//checkDisconnects(players)
	sendMessageToAll(players, "The game has started!")
	game, err := CreateGame(players)
	if err != nil {
		log.Fatal(err)
	}

	for {
		activePlayer := game.GetActivePlayer()
		sendPlayerMessage(activePlayer, "It is your turn, please enter some coordinates!")
		input, _ := readPlayerInput(activePlayer)
		var x, y string
		fmt.Sscan(input, &x, &y)
		fmt.Println(x, y)
		xx, _ := strconv.Atoi(x)
		yy, _ := strconv.Atoi(y)
		game.Move(xx, yy)
		//sendMessageToAll(players, string(game.board))
	}

	return nil
}

func sendMessageToAll(players []net.Conn, message string) error {
	for _, playerConn := range players {
		err := sendPlayerMessage(playerConn, message)
		if err != nil {
			return err
		}
	}
	return nil
}

func sendPlayerMessage(player net.Conn, message string) error {
	_, err := player.Write([]byte(message + "\n"))
	fmt.Println("Sending to player", message)
	if err != nil {
		fmt.Println(err)
		return err
	}
	return nil
}

/*
	Reads input from the player and returns it
*/
func readPlayerInput(player net.Conn) (message string, readError error){
	playerInput := make([]byte, 2048)
	inputLen, err := player.Read(playerInput)
	if err != nil {
		readError = err
		return
	}
	message = string(playerInput[:inputLen])

	return message, readError
}



/*
	Checks if any of the players has disconnected
 */
func checkDisconnects(players []net.Conn) error {
	for _, playerConn := range players {
		bytesRead, err := playerConn.Read(make([]byte, 10))
		fmt.Println("[DEBUG] Read", bytesRead, "when checking for DC")
		if err != nil{
			fmt.Println("Player has DC")
			return err
		}
	}

	return nil
}