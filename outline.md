Outline

**Problem Statement**

Finances Automation - no APIs

Explored requests, headless browser + Selenium, settled on PyAutoGUI (didn't want to get banned from financial services I use)

**PyAutoGUI**

- Learned about it from a pycon video by Al Sweigart (author)
- He emphasized that GUI automation can be *brittle* -- this demo is an example of that!
    - Dependent on OS, application version, user settings (ex: color themes, text size), physical monitor(s) / configuration (1080p vs 4k)


Some tricks:
- Can have PAG find images on screen
- Can take screenshots to find elements
    - CTRL+F, then look for solid color region of the CTRL+F color (usually, distinct!  Chrome = orange, FireFox = green)
- be careful about webpage encoding!  often run into iso-8859-1

**Main content**

Table, but not all the content is there when I inspect element!
Need to click individual links to load everything.

Once a link is clicked, the information stays on the page, even if the popup is hidden.

Show a GIF of this running!
    I want the GIF to be zoomed in so everyone can see, so I need to be able to run on a subset of the screen.