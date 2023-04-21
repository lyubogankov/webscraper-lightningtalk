# TITLE

## EXPLANATION

## Setup

### Reproducability
    
**GUI automation is closely tied to GUI being automated!**

I developed these sample scripts on Linux Mint / Chrome 97.  The GUI automation code tied to OS is within `download.py` - to get this running, you may need to modify for your own OS / color theme.

### Run code

1. Clone this repository locally.

2. Open `target.html` in Google Chrome.

3. Open command prompt and run `scrape.py`

    **Warning**
    * The Python script assumes that the prior foreground application (now the first background application) is Google Chrome.
    * `scrape.py` will press `ALT+TAB` one time to get Google Chrome into the foreground.
    * However, if you have interacted with other applications between steps 2 and 3, the script will not work as expected!



<!-- ## TODO

### Python:
- research minimum python version
- what are the requirements (package version wise)?  can I make a requirements.txt?

### Slides
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



'''
Not dealing with:
- error handling
    . what happens if the webpage doesn't download?
    . what happens if we are using the wrong encoding?
- centering the table
'''


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


-->