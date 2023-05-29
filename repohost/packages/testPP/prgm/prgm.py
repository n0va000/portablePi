import guilib as gui
from buttonlib import button
import time
import pputils as utils 
prgmName = "test package"
prgmDesc = "package test"
prgmAuthor = "test"
prgmMinSysVer = 0.2
prgmVer = 0
prgmIcon = ["1"]
def main():
    temp = gui.window("Connecting")
    Label1 = gui.window.label("Connecting...",0,64)
    Label1.draw()
    utils.wlan.connect()
    cycle = 0
    gui.clear()
    while 1:
        cycle += 1
        if utils.wlan.isConnected():
            break
        if cycle == 10:
            return "connection timed out"
        time.sleep(1)
    downArrow = ["00011000","00011000","00011000","11111111","11111111","01111110","00111100","00011000"]
    current = 0
    homeScreen = gui.window("app downloader", True, downArrow)
    exitScreen = gui.window("Want to exit?", True, downArrow)
    Label1 = gui.window.label("E. change window",0,16)
    nextLabel = gui.window.label("E. change window",0,64)
    while 1:
        gui.clear()
        nextLabel.draw()
        if button.E.isPressed():
            current += 1
        if current == 0:
            homeScreen.draw()
        elif current == 1:
            exitScreen.draw()
        else:
            current = 0
            




