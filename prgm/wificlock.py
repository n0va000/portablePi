
import os
import guilib as gui
import pputils as utils
from buttonlib import button
import time
prgmName = "clock"
prgmDesc = "gets time from wifi"
prgmAuthor = "system"
prgmVer = 0
prgmMinSysVer = 0.1
prgmIcon = ["1111111111111111",
            "1000000000000001",
            "1000000100000001",
            "1000000100000001",
            "1000000100000001",
            "1010000100000001",
            "1001000100000001",
            "1000100100000001",
            "1000010100000001",
            "1000001100000001",
            "1000000000000001",
            "1000000000000001",
            "1000000000000001",
            "1000000000000001",
            "1000000000000001",
            "1111111111111111"]
def main():
    utils.wlan.connect()
    cycle = 0
    gui.clear()
    gui.printAt("connecting",0,0)
    gui.update()
    while 1:
        cycle += 1
        if utils.wlan.isConnected():
            break
        if cycle == 10:
            return "connection timed out"
        time.sleep(1)
    while 1:
        gui.clear()
        gui.printAt("Downloading new time",0,0,1)
        timeJson = utils.wlan.wget("http://date.jsontest.com/")
        dateNow = timeJson["date"]
        timeNow = timeJson["time"]
        timeNums = timeNow.split(":")
        timeXM = timeNow[-2:]
        timeNow = timeNums[0]+" : "+timeNums[1]+" "+timeXM
        gui.update()
        gui.clear()
        gui.printAt(dateNow,0,0,1)
        gui.printAt(timeNow,0,8,2)
        gui.update()
        time.sleep(60)
