# TITLE

## EXPLANATION

## Setup

1. Clone this repository locally.

2. Open `target.html` in Google Chrome.

3. Open command prompt and run `scrape.py` (**what's the minimum python version**)

    **Warning**
    * The Python script assumes that the prior foreground application (now the first background application) is Google Chrome.
    * `scrape.py` will press `ALT+TAB` one time to get Google Chrome into the foreground.
    * However, if you have interacted with other applications between steps 2 and 3, the script will not work as expected!

## Reproduceability

This code was tested using the OS / Chrome versions below.  I do not guarantee it'll work with other setups.
- Linux Mint; Google Chrome 97.0.4692.99 64-bit
- Windows; Google Chrome 

## TODO
- research minimum python version
- what are the requirements (package version wise)?  can I make a requirements.txt?
- when recording GIF, increase my text-scaling (search for "fonts" in system), also use not-full-screen version of chrome (I want the GIF to be legible to everyone)
- make slides!