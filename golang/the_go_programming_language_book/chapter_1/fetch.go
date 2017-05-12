// Fetch prints the content found at a URL.
package main

import (
    "fmt"
    "net/http"
    "os"
	"io"
	"strings"
	"time"
	"io/ioutil"
)

func main() {
	start := time.Now()

    for _, url := range os.Args[1:] {
		// format url
		if !strings.HasPrefix(url, "http") {
			url = "http://" + url
		}

        resp, err := http.Get(url)
		if err != nil {
            fmt.Fprintf(os.Stderr, "fetch: %v\n", err)
            os.Exit(1)
        }

		fmt.Println("Received status code", resp.StatusCode)

		_, err2 := io.Copy(ioutil.Discard, resp.Body)
        resp.Body.Close()
        if err2 != nil {
            fmt.Fprintf(os.Stderr, "fetch: reading %s: %v\n", url, err2)
			os.Exit(1)
        }
		fmt.Println(url)
        //fmt.Printf("%s", b)
    }
	fmt.Printf("%.2fs elapsed\n", time.Since(start).Seconds())

}