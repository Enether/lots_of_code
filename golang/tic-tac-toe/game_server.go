package main

import (
	"net"
	"fmt"
)

func runGame(players []net.Conn) error {
	//checkDisconnects(players)
	sendMessageToAll(players, "The game has started!")
	return nil
}

func sendMessageToAll(players []net.Conn, message string) error {
	for _, playerConn := range players {
		_, err := playerConn.Write([]byte(message + "\n"))

		if err != nil {
			return err
		}
	}
	return nil
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