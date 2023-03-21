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

Python:
- research minimum python version
- what are the requirements (package version wise)?  can I make a requirements.txt?

Demo webpage:
- Do the HTML/CSS
- Research Javascript
    - https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Image_gallery
    - https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events
    - https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Adding_bouncing_balls_features
    - https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs
    - https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction
    - https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Manipulating_documents
    - https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Manipulating_documents
    - https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events
    - https://webplatform.github.io/docs/tutorials/your_first_look_at_javascript/#Where-to-put-JavaScript

- when recording GIF, increase my text-scaling (search for "fonts" in system), also use not-full-screen version of chrome (I want the GIF to be legible to everyone)
- make slides!