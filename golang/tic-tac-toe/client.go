package main

import (
	"net"
	"log"
	"fmt"
	"os"
	"bufio"
	"strings"
)

func main() {
	// establish conn
	conn, err := net.Dial("tcp", ":8080")
	if err != nil {
		log.Fatal(err)
	}

	for {
		message, err := bufio.NewReader(conn).ReadString('\n')
		if err != nil {
			log.Fatal(err)
		}

		fmt.Print(message)

		if strings.Contains(message, "Enter") {
			// read only when prompt
			reader := bufio.NewReader(os.Stdin)
			text, err := reader.ReadString('\n')
			if err != nil {
				log.Fatal(err)
			}

			fmt.Fprintf(conn, text+"\n")
		}
	}

	fmt.Println(conn)
}


