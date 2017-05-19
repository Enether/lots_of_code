package main

import (
	"flag"
	"fmt"
	"strings"
	"crypto/sha256"
	"crypto/sha512"
)

func main() {
	var wantedHash, input string
	flag.StringVar(&wantedHash, "hash", "SHA256", "The hash function you want to use. Supported functions: [SHA256 (default), SHA384, SHA512]")
	flag.Parse()
	wantedHash = strings.ToLower(wantedHash)

	fmt.Scanln(&input)

	if wantedHash == "" || wantedHash == "sha256" {
		// use the SHA256 hash
		fmt.Printf("%x\n", sha256.Sum256([]byte(input)))
	} else if wantedHash == "sha384" {
		fmt.Printf("%x\n", sha512.Sum384([]byte(input)))
	} else if wantedHash == "sha512" {
		fmt.Printf("%x\n", sha512.Sum512([]byte(input)))
	} else {
		fmt.Println("Invalid hash algorithm! Supported algorithms are SHA256, SHA384 and SHA512")
	}
}
