import time
from datetime import datetime

import pyautogui

def dl_to_known_location(_print=False, tempfilename=None, download_coords=None, save_coords=(805, 535), chrome_dlfooter_coords=(945, 520)):
    """Save file by controlling browser and file system, return filepath"""

    # save the webpage (assuming browser is foreground application)
    if _print:
        time.sleep(2)
        print(">>> pyautogui.hotkey('ctrl', 's', interval=0.1)")
    pyautogui.hotkey('ctrl', 's', interval=0.1)
    
    # For my operating system (Ubuntu-based Linux Mint), file explore opens after CTRL+S.  
    # I can immediately start writing the desired filename, then navigate to folder.
     
    # The file explorer popup appears in a consistent location based on the Chrome window's
    #  size / position, I hardcoded the needed coordinates.  To make this less brittle,
    #  you can take screenshots of file explorer GUI buttons and have pyautogui find those! 
    
    if tempfilename is None:
        tempfilename = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    if _print:
        time.sleep(0.5)
        print(f">>> pyautogui.write({repr(tempfilename)})")
    pyautogui.write(tempfilename)
    
    # the Downloads folder is already open, so no need to navigate anywhere.
    if download_coords:
        if _print:
            time.sleep(0.5)
            (f">>> pyautogui.click({download_coords})  # click Downloads folder")
        pyautogui.click(download_coords)

    if _print:
        time.sleep(0.5)
        print(f">>> pyautogui.click({save_coords})  # click Save")
    pyautogui.click(save_coords)

    if chrome_dlfooter_coords:
        if _print:
            time.sleep(0.5)
            print(f">>> pyautogui.click({chrome_dlfooter_coords})  # close downloads bar")
        pyautogui.click(chrome_dlfooter_coords)

    return f'/home/lyubo/Downloads/{tempfilename}.html'