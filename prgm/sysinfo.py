import sys
sys.path.insert(1,"/prgm")
sys.path.insert(1,"/system")
sys.path.insert(1,"/system/lib")
sys.path.insert(1,"/system/drivers")
import os
import guilib as gui
import pputils as utils
from buttonlib import button
import micropython
import gc
import time
prgmName = "system info"
prgmDesc = "system information"
prgmAuthor = "system"
prgmVer = 0
prgmMinSysVer = 0.1
prgmIcon = ["1111111111111111",
            "1000000000000001",
            "1000000000000001",
            "1000000000000001",
            "1000101010101001",
            "1001111111111001",
            "1001111111111001",
            "1001111111111001",
            "1001111111111001",
            "1001111111111001",
            "1001111111111001",
            "1000101010101001",
            "1000000000000001",
            "1000000000000001",
            "1000000000000001",
            "1111111111111111"]
def main():
    gui.clear()
    gui.printAt("Flash: "+str(os.statvfs("/")[0]/2)+"KB/"+str(os.statvfs("/")[3]/2)+"KB",0,0,1)
    gui.printAt("Ramdsk: "+"8.0KB/"+str(os.statvfs("/rbd")[3]/2)+"KB",0,8,1)
    gui.printAt("Ram: "+"264KB/"+str(gc.mem_free()/1000)+"KB",0,16,1)
    gui.printAt("Board: "+sys.platform,0,24,1)
    gui.printAt("Press A to continue",0,56,1)
    gui.update()
    while not button.A.isPressed():
        pass
    gui.clear()
    gui.printAt("Mpyver: "+os.uname()[2],0,0,1)
    gui.printAt("Pyver: "+sys.version,0,8,1)
    gui.printAt("Press A to continue",0,56,1)
    gui.update()
    while not button.A.isPressed():
        pass