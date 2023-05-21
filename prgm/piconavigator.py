import os
import guilib as gui
import pputils as utils
from buttonlib import button
import time
prgmName = "pico navigator!"
prgmDesc = "browse picosites"
prgmAuthor = "system"
prgmVer = 0
prgmMinSysVer = 0.1
prgmIcon = ["1111111111111111",
            "1000000000000001",
            "1001111100000001",
            "1000000011000001",
            "1000000000100001",
            "1000000000010001",
            "1000000000010001",
            "1000000000010001",
            "1000100000010001",
            "1001110000010001",
            "1000100000010001",
            "1000010000010001",
            "1000001111100001",
            "1000000000000001",
            "1000000000000001",
            "1111111111111111"]
def main():
    home = "https://raw.githubusercontent.com/n0va000/portablePico/main/picosite/home/index.pist"
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
    downloadSite(home)
    try:
        runSite()
        while 1:
            pass
    except Exception as E:
        gui.msgBox("SITE ERROR")
        print(E)

def darpy(url, path = "/rbd/", filename = "run"): # download and run py
    gui.clear()
    gui.printAt("downloading py script",0,0)
    gui.update()
    gui.clear()
    gui.update()
    f = open(path+filename+".py", "w")
    f.write(utils.wlan.wget(url, False).text)
    f.close()
    try:
    	exec("import "+filename)
    except:
    	gui.msgBox("PYTHON ERROR, the script has stopped")	
def downloadSite(url, file = "/rbd/current.pist"):
    gui.clear()
    gui.printAt("downloading site",0,0)
    gui.update()
    f = open(file, "w")
    f.write(utils.wlan.wget(url, False).text)
    f.close()

def runSite(file = "/rbd/current.pist"):
    f = open(file, "r")
    listsite = f.read()
    listsite = listsite.split("\n")
    f.close()
    print(listsite)
    line = 0
    if listsite[0]=="#PICOSITE":
        while 1:
            temp = runCommand(listsite[line], line, len(listsite)-1)
            line = temp 
            if line > len(listsite):
                break

    else:
        gui.msgBox("invalid site: non pico site")


def runCommand(command, line, length):
    try:
        if command[0]=="#":
            return line+1
        commandArgs = command.split(">")
        if commandArgs[0]=="msg":
            gui.msgBox("From site: "+commandArgs[1])
        elif commandArgs[0]=="txt":
            gui.printAt(commandArgs[4],int(commandArgs[2]),int(commandArgs[3]),int(commandArgs[1]))
        elif commandArgs[0]=="disp":
            if commandArgs[1]=="clear":
                gui.clear()
            if commandArgs[1]=="update":
                gui.update()
        elif commandArgs[0]=="ask":
            gui.msgBox("website wants to ask")
            if gui.ask(commandArgs[5],commandArgs[3],commandArgs[4]):
                return int(commandArgs[1])
            else:
                return int(commandArgs[2])
        elif commandArgs[0]=="gourl":
            downloadSite(commandArgs[1])
            runSite()
        elif commandArgs[0]=="go":
            return int(commandArgs[1])
        elif commandArgs[0]=="wb":
            if commandArgs[1]=="A":
                if button.A.isPressed():
                    return int(commandArgs[2])
            if commandArgs[1]=="B":
                if button.B.isPressed():
                    return int(commandArgs[2])
            if commandArgs[1]=="C":
                if button.C.isPressed():
                    return int(commandArgs[2])
            if commandArgs[1]=="D":
                if button.D.isPressed():
                    return int(commandArgs[2])
            if commandArgs[1]=="E":
                if button.E.isPressed():
                    return int(commandArgs[2])
        elif commandArgs[0]=="sleep":
            time.sleep(float(commandArgs[1]))
	elif commandArgs[0]=="py":
		gui.msgbox("website wants to run python")
		gui.msgbox("this can be dangerous!")
		if gui.ask("run python script?"):
			darpy(commandArgs[1])
    except Exception as E:
        gui.msgBox("site Command error")
        print(E)
    return line+1    
