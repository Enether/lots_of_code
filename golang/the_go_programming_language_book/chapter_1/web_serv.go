// Server2 is a minimal "echo" and counter server.
package main

import (
    "log"
    "net/http"
    "sync"
	"io"
	"image/gif"
	"image"
	"math"
	"math/rand"
	"image/color"
)
var palette = []color.Color{
	color.RGBA{0, 0, 0,255},
	color.Black,
	color.RGBA{0, 0, 255, 255},
	color.RGBA {255, 0, 0, 255}, color.RGBA{255, 57, 23, 25}}
var mu sync.Mutex
var count int
var chosenIdx int
var colors map[string]int = map[string]int{
	"red": 3,
	"blue": 2,
}
func main() {
	handler := func(w http.ResponseWriter, r *http.Request) {
		if err := r.ParseForm(); err != nil {
				log.Print(err)
		}
		chosenColor := r.Form["backgroundColor"]
		if chosenColorIdx := colors[chosenColor[0]]; chosenColorIdx != 0 {
			chosenIdx = chosenColorIdx
			lissajous(w, true)
		} else {
			lissajous(w, false)
		}
	}
    http.HandleFunc("/", handler)
    log.Fatal(http.ListenAndServe("localhost:8000", nil))
}


func lissajous(out io.Writer, chooseColor bool) {
	const (
		cycles= 5     // number of complete x oscillator revolutions
		res= 0.001 // angular resolution
		size= 100   // image canvas covers [-size..+size]
		nframes= 64    // number of animation frames
		delay= 8     // delay between frames in 10ms units
	)
	freq := rand.Float64() * 3.0 // relative frequency of y oscillator
	anim := gif.GIF{LoopCount: nframes}
	phase := 0.0 // phase difference
	for i := 0; i < nframes; i++ {
		rect := image.Rect(0, 0, 2*size+1, 2*size+1)
		img := image.NewPaletted(rect, palette)
		for t := 0.0; t < cycles*2*math.Pi; t += res {
			x := math.Sin(t)
			y := math.Sin(t*freq + phase)
			if chooseColor {
				img.SetColorIndex(size+int(x*size+0.5), size+int(y*size+0.5),
				uint8(chosenIdx))
			} else {
			img.SetColorIndex(size+int(x*size+0.5), size+int(y*size+0.5),
				uint8(rand.Int()%5))
			}

		}
		phase += 0.1
		anim.Delay = append(anim.Delay, delay)
		anim.Image = append(anim.Image, img)
	}
	gif.EncodeAll(out, &anim) // NOTE: ignoring encoding errors
}


