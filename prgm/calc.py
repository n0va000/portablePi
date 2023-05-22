import guilib as gui
import pputils as utils
from buttonlib import button
import time
prgmName = "calc"
prgmDesc = "calculator"
prgmAuthor = "system"
prgmVer = 0
prgmMinSysVer = 0.2
prgmIcon = ["1111111111111111",
            "1000000000000001",
            "1011110001010101",
            "1000000000000001",
            "1111111111111111",
            "1000000000000001",
            "1000000000000001",
            "1001000010100001",
            "1011100001000001",
            "1001000010100001",
            "1000000000000001",
            "1000000001001001",
            "1011110000100001",
            "1000000010010001",
            "1000000000000001",
            "1111111111111111"]
def main():
    gui.cli.auto = True
    calc = True
    while calc:
    	try:
    		ans = eval(gui.osk("sum","0123456789*-+/0"))
    		gui.splash("awnser: "+str(ans),1)
    	except Exception as E:
    		gui.splash("ERROR: "+str(E),1)
    	if gui.ask("do what","exit","again"):
    		calc = False
