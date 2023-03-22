import pdb
import time
from pprint import pprint

import easyocr                  # https://pypi.org/project/easyocr/
import mss                      # https://pypi.org/project/mss/
import pyautogui                # https://pypi.org/project/PyAutoGUI/
from bs4 import BeautifulSoup   # https://pypi.org/project/beautifulsoup4/
from fuzzywuzzy import fuzz     # https://pypi.org/project/fuzzywuzzy/
from PIL import Image           # https://pypi.org/project/Pillow/

import download

# raising default PAUSE time to avoid time.sleep() between pyautogui commands
pyautogui.PAUSE = 1  # default = 0.1s

def parse_webpage(webpage, parser='html.parser'):
    """Open provided webpage and parse using BeautifulSoup."""
    with open(webpage, 'r', encoding='utf-8') as f:
        return BeautifulSoup(f, parser)

def extract_transaction_info(soup):
    """Extract desired information from HTML page (description text and payment method)."""
    tx_table = soup.find('tbody')
    descriptions = [desc.text for desc in tx_table.find_all('td', class_='description')]
    payment_methods = [paym.text for paym in tx_table.find_all('td', class_='paymethod')]
    return descriptions, payment_methods

def print_extracted(descriptions, payment_methods):
    """Print out per-transaction description and payment method."""
    current_state = 'BEFORE' if all(paym == "" for paym in payment_methods) else 'AFTER'
    print(f'{current_state} LINK CLICKING:')
    for desc, paymethod in zip(descriptions, payment_methods):
        print(f'\t{desc:>12} {paymethod}')

def take_cropped_screenshot(top, left, width, height, outputname='screenshot.png'):
    """Take a screenshot of a portion of the screen."""
    with mss.mss() as screenshotter:
        monitor = {'top': top, 'left': left, 'width': width, 'height': height}
        image = screenshotter.grab(monitor)
        mss.tools.to_png(image.rgb, image.size, output=outputname)
    return outputname

def easyocr_to_pyautogui_coords(easyocr_boundingbox):
    """Convert easyocr boundingbox to pyautogui boundingbox."""
    #   top left, top right, bot right, bot left
    ((tl_x, tl_y), (tr_x, _), (_, _), (_, bl_y)) = easyocr_boundingbox
    return (tl_x, tl_y, tr_x - tl_x, bl_y - tl_y)

def center_and_click(pyautogui_boundingbox):
    """Compute boundingbox's center (x, y) and click that point (convinience function)."""
    pyautogui.click(
        pyautogui.center(
            pyautogui_boundingbox
        )
    )

def scrape():
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
    descriptions, payment_methods = extract_transaction_info(soup)
    print_extracted(descriptions, payment_methods)

    # take screenshot, crop
    OFFSET_TOP, OFFSET_LEFT = 150, 480
    screenshot = take_cropped_screenshot(top=OFFSET_TOP, left=OFFSET_LEFT, width=480, height=530)

    # perform OCR
    ocr_reader = easyocr.Reader(['en'], gpu=False)
    ocr_results = ocr_reader.readtext(screenshot)
    print('------------\nOCR Results:')
    pprint(ocr_results)
    print('------------')

    # match descriptions to OCR results, click all the links
    ocr_results = iter(ocr_results)  # list -> iterator
    for i, desc in enumerate(descriptions):
        while True:
            ocrboundingbox, text, _ = next(ocr_results)  # not handling StopIteration exception
            # offset our screenshot to get real screen coords!
            x, y, width, height = easyocr_to_pyautogui_coords(ocrboundingbox)
            realboundingbox = (x + OFFSET_LEFT, y + OFFSET_TOP, width, height)

            similarity = fuzz.partial_ratio(desc.lower(), text.lower())  # [0, 100]
            print(f'\t{desc:>12} {text:>12} [{similarity}% match]')
            if similarity > 80:
                # open the hidden row to load the extra text content
                center_and_click(realboundingbox)
                time.sleep(2)
                # close the hidden row so the boundingboxes we found are still valid!
                center_and_click(realboundingbox)
                break

    # download again, and parse!
    soup = parse_webpage(download.dl_to_known_location())
    print_extracted(*extract_transaction_info(soup))

if __name__ == '__main__':
    scrape()

'''
example.png

Draw bounding boxes around the OCR results -- show easyocr's behavior!

OCR results:

[([[15, 21], [119, 21], [119, 61], [15, 61]], 'Pycon', 0.6994198329365593),
 ([[133, 21], [257, 21], [257, 57], [133, 57]], 'ticket', 0.9999962526402947),
 ([[13, 87], [159, 87], [159, 129], [13, 129]], 'Lodging', 0.9999927908914014),
 ([[15, 155], [179, 155], [179, 195], [15, 195]],
  'Airplane',
  0.8327755179002724),
 ([[193, 155], [337, 155], [337, 191], [193, 191]],
  'tickets',
  0.9999943228283826),
 ([[15, 223], [217, 223], [217, 259], [15, 259]],
  'Restaurant',
  0.9999608935635564),
 ([[14, 292], [198, 292], [198, 324], [14, 324]],
  'Groceries',
  0.9999074914518178),
 ([[14, 358], [158, 358], [158, 390], [14, 390]],
  'Transit',
  0.9059198505865829),
 ([[173, 355], [257, 355], [257, 391], [173, 391]], 'fare', 0.9999932050704956),
 ([[13, 423], [199, 423], [199, 459], [13, 459]],
  'Groceries',
  0.9999418250206089)]
'''

'''
Not dealing with:
- error handling
    . what happens if the webpage doesn't download?
    . what happens if we are using the wrong encoding?
- centering the table
- cleanup (deleting the downloaded webpage)
'''

'''
1. Download the page using BeautifulSoup

2. num_pending_rows, found_prev_newest_temp = \
        self.extract_main_page_transactions(rows, page_extracted, prev_newest_tx_dict)
                                                  ^ starts as []
    loop over all rows:
        - skip pending
        - extract visible info (post date, amount, description) -- append to page_extracted

3. page_extracted, found_prev_newest = \
        self.click_all_description_links(
            num_rows, num_pending_rows, page_extracted, prev_newest_tx_dict
        )

    * assumption: the entire table fits onto the screen and multiple screenshots are not required

    a. Calculate which column we should ctrl-f for, so we can center the table
        Has to be off the screen!

    b. ocr_results_list, y_offset = self.cc_tx_screenshot_and_ocr(...)

        - Center the table
            - If there are 5 or fewer tx (non-pending) rows, center the table by CTRL+F "Go to", which is at page bottom
            - Otherwise, CTRL+F w/ (row balance of prior element, then) description text of center row (disambiguate repeats)
        - Find boundingbox of pending rows - we want the bottom bound so that we can exclude that from our screenshot
        - Take cropped screenshot!  Should just be of the non-pending transaction descriptions
        - Pass cropped screenshot through OCR reader

    c. Match screenshot results with description text from each row
        - Loop over the rows, and try to match the OCR results.  Treating the OCR results as an iterator and calling `next()`
            - Keep calling `next()` until we have a good enough match -- fuzz.partial_ratio(desc.lower(), ocr_text.lower())
            - Capture its bounding box! (It's in EasyOCR coordinates)

            - Click on the link (`pyautogui.click(pyautogui.center(boundingbox))`)

            - If needed, close the results box by clicking it again (for those at/below the center)

4. self.extract_main_page_tx_details(page_extracted)
    `zip` the page_extracted / OCR results and process the data from the expanded links.

'''