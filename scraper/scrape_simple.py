import os
import shutil
import time

import pyautogui                # https://pypi.org/project/PyAutoGUI/
from bs4 import BeautifulSoup   # https://pypi.org/project/beautifulsoup4/

import download

# raising default PAUSE time to avoid time.sleep() between pyautogui commands
pyautogui.PAUSE = 1  # default = 0.1s


def scrape(verbose=False):
    """Demo of core PyAutoGUI scraping workflow:
    CTRL+S to save locally, parse with BeautifulSoup.
    """
    
    # ALT-TAB to browser
    # os.system('clear')
    time.sleep(2)
    print(r">>> pyautogui.hotkey('alt', '\t', interval=0.1)")
    pyautogui.hotkey('alt', '\t', interval=0.1)

    # download the web page
    webpage = download.dl_to_known_location(
        _print=True, tempfilename='simple', save_coords=(470, 540), chrome_dlfooter_coords=None)
    
    # parse!
    time.sleep(1)
    print()
    print(">>> with open('simple.html', 'r', encoding='utf-8') as f:")
    print("...     soup = BeautifulSoup(f, 'html.parser')")
    with open(webpage, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    time.sleep(4)
    print()
    print(">>> soup.find('p').text")
    print(repr(soup.find('p').text))
    print('\n\n\n')

    # clean up
    os.remove(webpage)                                 # html file
    shutil.rmtree(webpage.replace('.html', '_files'))  # supporting folder

if __name__ == '__main__':
    time.sleep(1)
    print('>>> import pyautogui')
    print('>>> from bs4 import BeautifulSoup')
    print()
    scrape()