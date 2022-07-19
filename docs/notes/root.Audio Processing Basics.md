---
id: u7ry7olukcxdqe2a5y6298p
title: Audio Processing Basics
desc: ''
updated: 1655763498132
created: 1655760309768
---

## Audio File Formats

Three most popular ones

- .mp3: its a lossy compression format, it means it compresses the data and during this process, we can lose information.
- .flac: is a loss less compression format, also compresses the data but allows us to perfectly reconstruct the original data.
- .wav: is a uncompressed format, it means it stores the data in an uncmpressed way. Audio Quality is the best but also the file size is the largest. WAV is the standard for CD audio quality.

## Audio Signal Parameters

- number of channels: usually one or two. one is known as mono and two is stereo. So this is the number of independent audio channels.
Example - two or stereo has two independent channels, it gives you the impression that the audio is coming from two different directions.
- Sample width: Number of bytes for each sample
- framerate/sample_rate: also known as sample frequency. A very important parameter. It means number of samples for each second.
Example - 44,100 Hz or 44.1 kilohertz -> standard sampling rate for CD quality. This means we get 44,100 sample values in each second.
- number of frames: Toatal number of frames we get
- values of a frame: Values in each frame, when we load this, it will be in a binary format, but we can convert this to integer values later.

## Wave Module

To show how to load and save a WAV file -> **Check wave_example.py**

## How to plot a wave signal

-> **plot_audio.py**

## How to do a microphone recording in Python

## How to load other file formats like mp3 files
