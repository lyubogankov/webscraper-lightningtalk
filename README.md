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

## TODO

### Python:
- research minimum python version
- what are the requirements (package version wise)?  can I make a requirements.txt?

### Slides
- Finish last several
- Add animations
- After I have a final draft, export as PDF and put into repo

### Update README -- document tips/tricks/warnings nicely (draft below)

**Warnings**

- With easyocr, each word usually has its own bounding box.  you may need to process easy-ocr's output further (ex: group words that have approx same y-coords into same row, space-delimited)
    Show annotated screenshot!

- pyautogui, PIL, easyocr all have different boundingbox coordinate "systems"

- Fuzzywuzzy: match OCR results with description text
In the slides - give example of real description vs real OCR'd and fuzzywuzzy results since the example is "clean"?

- Be careful about webpage encoding!  often run into iso-8859-1

**Tips and Tricks**

- Can have PAG find images on screen (either pixel-perfect match or with OpenCV - can specify % confidence threshold) (*mentioned in presentation*)
- Can take screenshots to find elements
    - CTRL+F, then look for solid color region of the CTRL+F color (usually, distinct!  Chrome = orange, FireFox = green)


## Linksave
- https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Image_gallery
- https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events
- https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Adding_bouncing_balls_features
- https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs
- https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction
- https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Manipulating_documents
- https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Manipulating_documents
- https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events
- https://webplatform.github.io/docs/tutorials/your_first_look_at_javascript/#Where-to-put-JavaScript