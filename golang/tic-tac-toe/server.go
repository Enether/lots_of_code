package main

import (
	"net"
	"fmt"
	"log"
)

const NEEDED_PLAYERS = 2

func main() {
	var currPlayers []net.Conn  // holds the current connecter players
	ln, err := net.Listen("tcp", ":8080")
	if err != nil {
		log.Fatal(err)
	}

	for {
		conn, conErr := ln.Accept()
		if conErr != nil {
			log.Fatal(conErr)
		}
		fmt.Println(conn)

		conn.Write([]byte(fmt.Sprintf("Conneted to the game server!\nWaiting for one more player...")))
		currPlayers = append(currPlayers, conn)

		if len(currPlayers) == NEEDED_PLAYERS {
			// start off a game
			// continue accepting more players
			go startGame(currPlayers)
			currPlayers = nil
		}
	}
}

func startGame(players []net.Conn) {
	fmt.Println("Started a game!")
	for _, player := range players {
		fmt.Println(player)
	}

	runGame(players)
}