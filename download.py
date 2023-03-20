import time
from datetime import datetime

import pyautogui

def dl_to_known_location() -> str:
    """Saves file by controlling browser and file system, returns filepath"""

    pyautogui.PAUSE = 2  # 0.1s -> 2s

    # save the webpage (assuming browser is foreground application)
    with pyautogui.hold('ctrl'):
        pyautogui.press('s')

    # For my operating system (Ubuntu-based Linux Mint), file explore opens after CTRL+S.  
    # I can immediately start writing the desired filename, then navigate to folder.
     
    # The file explorer popup appears in a consistent location based on the Chrome window's
    #  size / position, I hardcoded the needed coordinates.  To make this less brittle,
    #  you can take screenshots of file explorer GUI buttons and have pyautogui find those! 
    
    tempfilename = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    pyautogui.write(tempfilename)

    pyautogui.click((170,  370))  # click Downloads on the sidebar
    pyautogui.click((830,  700))  # click Save
    pyautogui.click((940, 1020))  # close Chrome downloads footer

    pyautogui.PAUSE = 1  # 0.1s -> 2s

    return f'/home/lyubo/Downloads/{tempfilename}.html'