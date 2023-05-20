sysver = 0.1
if __name__=="__main__":
    import sys
    sys.path.insert(1,"/prgm")
    sys.path.insert(1,"/system/lib")
    sys.path.insert(1,"/system")
import guilib as gui
import time
import pputils as utils
import gc
try:
    import userdata as user
    username = user.name
    usericon = user.icon
    wifiState = user.netCred.state
    utils.wlan.setState(wifiState)
except:
    emptyByte = "0"*8
    fullByte = "1"*8
    username = "failed"
    usericon = utils.pholderImg(8,8)
    userfailed = True
    gui.msgBox("USERDAT FAIL")
    wifiState = True
    utils.wlan.setState(wifiState)
utils.wlan.connect()
import os
from buttonlib import button
prgmName = "hscreen"
prgmDesc = "..."
prgmAuthor = "system"
prgmVer = 0.1
prgmIcon = ["1111111111111111",
            "1000000000000001",
            "1010000000000001",
            "1010000000000001",
            "1011100000000001",
            "1010100000000001",
            "1010100000000001",
            "1000000000000001",
            "1001110000000001",
            "1010000000000001",
            "1001100000000001",
            "1000010000000001",
            "1001100000000001",
            "1000000000000001",
            "1000000000000001",
            "1111111111111111"]
emptyIcon = ["1111111111111111",
            "1000000000000001",
            "1000000000000001",
            "1000000000000001",
            "1000000000000001",
            "1000000000000001",
            "1000000000000001",
            "1000000000000001",
            "1000000000000001",
            "1000000000000001",
            "1000000000000001",
            "1000000000000001",
            "1000000000000001",
            "1000000000000001",
            "1000000000000001",
            "1111111111111111"]
wifiConIcon = ["00000000",
               "00000000",
               "11000000",
               "00110000",
               "00001000",
               "11001000",
               "00100100",
               "10100100"]
wifiDisconIcon = ["00000000",
                  "00101000",
                  "00010000",
                  "00101000",
                  "10000000",
                  "10000000",
                  "00000000",
                  "10000000"]
wifiOffIcon = ["00000000",
               "00101000",
               "00010000",
               "00101000",
               "00000000",
               "00000000",
               "00000000",
               "00000000"]
def setApp(appid):
    appid = str(appid)
    try:
        exec("import prgm"+appid)
        exec("prgm"+appid+"Name = prgm"+appid+".prgmName")
        exec("prgm"+appid+"Desc = prgm"+appid+".prgmDesc")
        exec("prgm"+appid+"Author = prgm"+appid+".prgmAuthor")
        exec("prgm"+appid+"Ver = prgm"+appid+".prgmVer")
        exec("prgm"+appid+"Icon = prgm"+appid+".prgmIcon")
        exec("prgm"+appid+"Minsv = prgm"+appid+".prgmMinSysVer")
    except Exception as E:
        print(E)
        exec("prgm"+appid+"Name = 'ERROR'")
        exec("prgm"+appid+"Desc = 'ERROR'")
        exec("prgm"+appid+"Author = 'ERROR'")
        exec("prgm"+appid+"Ver = 0")
        exec("prgm"+appid+"Icon = emptyIcon")
        exec("prgm"+appid+"Minsv = 0")
for i in range(len(os.listdir("/prgm/"))):
    setApp(i+1)
def updateGui(sel, username,maxLen):
        gui.clear()
        if wifiState:
            if utils.wlan.isConnected():
                gui.drawImg(wifiConIcon,xpos = 120, ypos = 2, xsize = 8, ysize = 8)
            else:
                gui.drawImg(wifiDisconIcon,xpos = 120, ypos = 2, xsize = 8, ysize = 8)
        else:
            gui.drawImg(wifiOffIcon ,xpos = 120, ypos = 2, xsize = 8, ysize = 8)
        gui.drawImg(usericon,xpos = 2, ypos = 2, xsize = 8, ysize = 8)
        gui.drawImg(eval("prgm"+str(sel)+"Icon"),xpos = 13, ypos = 16, xsize = 16, ysize = 16)
        # top
        gui.drawLine(0,0,gui.WIDTH,0)
        gui.drawLine(0,11,gui.WIDTH,11)
        # side
        gui.drawLine(11,0,11,gui.HEIGHT)
    
        gui.printAt(username+"'s homescreen",13,1,1)
        gui.printAt(eval("prgm"+str(sel)+"Name"),32,18,1)
        gui.printAt(eval("prgm"+str(sel)+"Desc"),32,26,1)
        gui.printAt(str(eval("prgm"+str(sel)+"Ver")),12,56,1)
        # page num
        gui.printAt(str(int(len(maxLen))),0,56,1)
        gui.printAt("/",0,48,1)
        gui.printAt(str(sel),0,40,1)
        if sel == len(maxLen):
            gui.drawImg(emptyIcon,xpos = 13, ypos = 34, xsize = 16, ysize = 16)
            gui.printAt("back to top",32,36,1)
            gui.printAt("no more app",32,44,1)
        else:
            gui.drawImg(eval("prgm"+str(sel+1)+"Icon"),xpos = 13, ypos = 34, xsize = 16, ysize = 16)
            gui.printAt(eval("prgm"+str(sel+1)+"Name"),32,36,1)
            gui.printAt(eval("prgm"+str(sel+1)+"Desc"),32,44,1)
        gui.printAt(">>",1,18,1)
        gui.update()
def main():
    gui.cli.auto = False
    maxLen = os.listdir("/prgm/")
    gui.msgBox("Welcome "+username)
    sel = 1
    updateGui(sel, username, maxLen)
    cycle = 0
    while True:
        cycle += 1
        if button.A.isPressed():
            try:
                if sysver+0.1 > eval("prgm"+str(sel)+"Minsv"):
                    gui.cli.printl("running "+eval("prgm"+str(sel)+"Name")+"V"+str(eval("prgm"+str(sel)+"Ver")))
                    temp = eval("prgm"+str(sel)+".main()")
                    gui.cli.auto = True
                    gui.cli.printl("garbage collecting...")
                    gc.collect()
                    gui.cli.auto = False
                    if not temp==None:
                        gui.msgBox("program returned")
                        gui.msgBox("ret: "+str(temp))
                else:
                    gui.msgBox("prgm for "+str(eval("prgm"+str(sel)+"Minsv"))+" and newer, cannot run on "+str(sysver))
            except Exception as E:
                print(E)
                gui.cli.auto = True
                gui.cli.printl("ERROR PRGM CRASH:")
                gui.cli.printl(str(E))
                gui.cli.printl("garbage collecting...")
                gc.collect()
                gui.cli.printl("press a to return home")
                gui.cli.auto = False
                while True:
                    if button.A.isPressed(): 
                        break
                gui.msgBox("program crashed!")
            updateGui(sel, username, maxLen)
        if button.D.isPressed():
            sel -= 1
            if sel == 0:
                sel = len(maxLen)
            updateGui(sel, username, maxLen)
        if button.E.isPressed():
            sel += 1
            if sel == len(maxLen)+1:
                sel = 1
            updateGui(sel, username, maxLen)
        if cycle == 1000:
            cycle = 0
            updateGui(sel, username, maxLen)

