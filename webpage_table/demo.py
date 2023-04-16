import time
import pyautogui

def demo_table():
    while(True):
        # expand first, then second;  collapse first, then second
        for x, y in [(375, 300), (375, 490), (375, 300), (375, 390)]:
            pyautogui.moveTo(x=x, y=y, duration=1.5, tween=pyautogui.easeOutQuad)  # start fast, end slow
            pyautogui.click()

def demo_woe():
    time.sleep(7)
    for x, y, duration, delay_after in [( 343, 272, 2, 2),  # webpage:   click on Q1 row 
                                        (1013, 561, 2, 5)]: # inspector: html table row Q1 content expand
        pyautogui.moveTo(x=x, y=y, duration=duration, tween=pyautogui.easeOutQuad)  # start fast, end slow
        pyautogui.click()
        time.sleep(delay_after)

if __name__ == '__main__':
    demo_table()