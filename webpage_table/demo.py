import time
import pyautogui

def demo_table():
    while(True):
        # expand first, then second;  collapse first, then second
        for x, y in [(375, 300), (375, 490), (375, 300), (375, 390)]:
            pyautogui.moveTo(x=x, y=y, duration=1.5, tween=pyautogui.easeOutQuad)  # start fast, end slow
            pyautogui.click()

def demo_woe():
    for x, y, duration, delay_after in [( 980, 400, 1, 3),  # inspector: html table row Q1 expand
                                        ( 980, 400, 0, 1),  # inspector: html table row Q1 collapse
                                        ( 980, 440, 1, 2),  # inspector: html table row A1 expand
                                        ( 343, 272, 2, 2),  # webpage:   click on Q1 row 
                                        (1013, 481, 2, 5)]: # inspector: html table row Q1 content expand
        pyautogui.moveTo(x=x, y=y, duration=duration, tween=pyautogui.easeOutQuad)  # start fast, end slow
        pyautogui.click()
        time.sleep(delay_after)

if __name__ == '__main__':
    demo_woe()