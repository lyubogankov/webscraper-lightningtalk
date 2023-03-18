# standard library
import time
from datetime import datetime
# third-party
import pyautogui

def dl_to_known_location() -> str:
    """Saves file by controlling browser and file system, returns filepath"""

    # save the webpage (assuming browser is foreground application)
    with pyautogui.hold('ctrl'):
        pyautogui.press('s')
    time.sleep(2)

    # For my operating system (Ubuntu-based Linux Mint), file explore opens after CTRL+S.  
    # I can immediately start writing the desired filename, then navigate to folder.
     
    # The file explorer popup appears in a consistent location based on the Chrome window's
    #  size / position, I hardcoded the needed coordinates.
    
    tempfilename = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    pyautogui.write(tempfilename)

    # click Downloads on the sidebar

    # click Save

    # close Chrome downloads footer

    return f'/home/lyubo/Downloads/{tempfilename}.html'