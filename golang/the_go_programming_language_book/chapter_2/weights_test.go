package main

import "testing"
import   "github.com/stretchr/testify/assert"

func TestKilogram_ToLBS(t *testing.T) {
	var givenKG Kilogram = 100
	var expectedLBS Pound = 220

	assert.Equal(t, expectedLBS, givenKG.ToLBS())
}

func TestPounds_ToKG(t *testing.T) {
	var givenLBS Pound = 220
	var expectedKG Kilogram = 100

	assert.Equal(t, expectedKG, givenLBS.ToKG())
}
