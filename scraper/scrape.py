import itertools
import os
import pdb
import shutil
import time
from pprint import pprint

import easyocr                  # https://pypi.org/project/easyocr/
import mss                      # https://pypi.org/project/mss/
import pyautogui                # https://pypi.org/project/PyAutoGUI/
from bs4 import BeautifulSoup   # https://pypi.org/project/beautifulsoup4/
from fuzzywuzzy import fuzz     # https://pypi.org/project/fuzzywuzzy/

import download

# raising default PAUSE time to avoid time.sleep() between pyautogui commands
pyautogui.PAUSE = 1  # default = 0.1s

def parse_webpage(webpage, parser='html.parser', cleanup=True):
    """Open provided webpage and parse using BeautifulSoup."""
    with open(webpage, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, parser)
    if cleanup:
        os.remove(webpage)                                 # html file
        shutil.rmtree(webpage.replace('.html', '_files'))  # supporting folder
    return soup

def extract_info(soup):
    """Extract desired information from HTML page (question / answer pairs)."""
    tx_table = soup.find('tbody')
    questions = [q.text for q in tx_table.find_all('th', class_='question')]
    answers = [a.text for a in tx_table.find_all('th', class_='answer')]
    return questions, answers

def print_extracted(questions, answers):
    """Print out question/answer pairs."""
    current_state = 'BEFORE' if all(a == "" for a in answers) else 'AFTER'
    print(f'{current_state} LINK CLICKING:')
    for q, a in zip(questions, answers):
        print(f'\t{q:<15} {a}')

def take_cropped_screenshot(top, left, width, height, outputname='screenshot.png'):
    """Take a screenshot of a portion of the screen."""
    with mss.mss() as screenshotter:
        monitor = {'top': top, 'left': left, 'width': width, 'height': height}
        image = screenshotter.grab(monitor)
        mss.tools.to_png(image.rgb, image.size, output=outputname)
    return outputname

def pairwise(iterable):
    """https://docs.python.org/3/library/itertools.html#itertools.pairwise (new in 3.10)
    Roughly equivalent to:
    """
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

def consolidate_ocr_results_into_rows(ocr_results):
    """Turn per-word OCR boundingboxes/text into per-row boundingboxes/text.
    (English) OCR results are returned top-to-bottom, left-to-right.

    Expressed in constants below:
    OCR results format: [boundingbox, text: str, conficence: float]
           boundingbox: [point_topleft, point_topright, point_botright, point_botleft]
               point_*: [x: int, y: int]
    """
    TOLERANCE = 5  # pixels
    BB, TEXT = 0, 1
    TOPL, TOPR, BOTR, BOTL = 0, 1, 2, 3
    X, Y = 0, 1
    # Initialize with 1 row -- the first result's boundingbox and text
    rows = [[ocr_results[0][BB], ocr_results[0][TEXT]]]
    for (bb1, _, _), (bb2, text2, _) in pairwise(ocr_results):
        # if bottom edges are close, consider them part of the same row
        if abs(bb1[BOTR][Y] - bb2[BOTL][Y]) <= TOLERANCE:
            rows[-1][BB][BOTR] = bb2[BOTR]
            rows[-1][BB][TOPR] = bb2[TOPR]
            rows[-1][TEXT] += ' ' + text2
        # otherwise, new row!
        else:
            rows.append([bb2, text2])
    return rows

def easyocr_to_pyautogui_coords(easyocr_boundingbox):
    """Convert easyocr boundingbox to pyautogui boundingbox."""
    #   top left, top right, bot right, bot left
    ((tl_x, tl_y), (tr_x, _), (_, _), (_, bl_y)) = easyocr_boundingbox
    return (tl_x, tl_y, tr_x - tl_x, bl_y - tl_y)

def prettify_easyocr_bb(boundingbox):
    """Print boundingbox string nicely, so that multiple lines match up.
    Hardcoding num_digits=3
    """
    retstr = '['
    for i, (x, y) in enumerate(boundingbox):
        retstr += f'[{x:>3}, {y:>3}]'
        if i != len(boundingbox) - 1:
            retstr += ', '
    retstr += ']'
    return retstr

def center_and_click(pyautogui_boundingbox):
    """Compute boundingbox's center (x, y) and click that point (convinience function)."""
    pyautogui.click(
        pyautogui.center(
            pyautogui_boundingbox
        )
    )

def scrape(verbose=False):
    """Clicks links to load additional content, then scrapes webpage.
    
    Problem statement:
    Want to scrape table, but not all information is loaded with the page.
    Need to specifically click links to obtain all information.

    In order to run this code, please follow the repo README instructions.
    """
    
    # ALT-TAB to browser
    with pyautogui.hold('alt'):
        pyautogui.press('\t')

    # initial download/parse
    webpage = download.dl_to_known_location()
    soup = parse_webpage(webpage)
    questions, answers = extract_info(soup)
    print_extracted(questions, answers)

    # take screenshot, crop
    OFFSET_TOP, OFFSET_LEFT = 227, 42  # y, x
    screenshot = take_cropped_screenshot(top=OFFSET_TOP, left=OFFSET_LEFT, width=878, height=310)

    # perform OCR, group results into rows
    ocr_reader = easyocr.Reader(['en'], gpu=False)
    ocr_results = ocr_reader.readtext(screenshot)
    print('------------')
    if verbose:
        print('OCR Results:')
        for ocrboundingbox, text, confidence in ocr_results:
            print(f'[{confidence:.2f}] {text:<9} {prettify_easyocr_bb(ocrboundingbox)}')
        print('------------')
    ocr_rows = consolidate_ocr_results_into_rows(ocr_results)
    print('OCR Rows:')
    for ocrboundingbox, text in ocr_rows:
        print(f'{text:<15} {prettify_easyocr_bb(ocrboundingbox)}')
    print('------------')

    # match questions to OCR results, click all the links
    print('MATCHING EXTRACTED <-> OCR:')
    ocr_rows = iter(ocr_rows)  # list -> iterator
    for i, q in enumerate(questions):
        while True:
            ocrboundingbox, text = next(ocr_rows)  # not handling StopIteration exception
            # offset our screenshot to get real screen coords!
            x, y, width, height = easyocr_to_pyautogui_coords(ocrboundingbox)
            realboundingbox = (x + OFFSET_LEFT, y + OFFSET_TOP, width, height)

            similarity = fuzz.partial_ratio(q.lower(), text.lower())  # [0, 100]
            print(f'\t{q:>15} {text:>15} [{similarity}% match]')
            if similarity > 80:
                # open the hidden row to load the extra text content
                center_and_click(realboundingbox)
                time.sleep(2)
                # close the hidden row so the boundingboxes we found are still valid!
                center_and_click(realboundingbox)
                break

    # download again, and parse!
    soup = parse_webpage(download.dl_to_known_location())
    print_extracted(*extract_info(soup))

if __name__ == '__main__':
    scrape()

'''
example.png

Draw bounding boxes around the OCR results -- show easyocr's behavior!

OCR results:
[[3, 17], [323, 17], [323, 83], [3, 83]]
[1.00] Favorite
[[352, 6], [603, 6], [603, 86], [352, 86]]
[0.60] color2
[[0, 105], [324, 105], [324, 178], [0, 178]]
[1.00] Favorite_
[[351, 97], [564, 97], [564, 181], [351, 181]]
[0.71] food2
'''

'''
Not dealing with:
- error handling
    . what happens if the webpage doesn't download?
    . what happens if we are using the wrong encoding?
- centering the table
'''