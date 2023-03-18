# standard library

# third-party
import easyocr
import pyautogui
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz
from mss import mss
from PIL import image
# local
import download

def download_webpage():
    """Download """
    pass

def scrape():
    """Clicks links to load additional content, then scrapes webpage.
    
    Problem statement:
    Want to scrape table, but not all information is loaded with the page.
    Need to specifically click links to obtain all information.

    In order to run this code, please follow the repo README instructions.
    """
    
    # 0. ALT-TAB to browser
    with pyautogui.hold('alt'):
        pyautogui.press('\t')

    # 1. download initially
    webpage = download.dl_to_known_location()
    
    # 2. parse using BS4 - extract description text
    with open(webpage, encoding='utf-8', 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')  # can also use lxml per BS docs

    # 3. center the table

    # 4. take screenshot, crop
    screenshotter = mss()

    # 5. perform OCR
    ocr_reader = easyocr.Reader(['en'], gpu=False)

    # 6. match OCR results with description text (fuzzywuzzy)

    # 7. click all the links

    # 8. download again, and parse!

    # 9. return parsed info

    pass

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