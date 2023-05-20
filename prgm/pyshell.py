import guilib as gui
import pputils as utils
from buttonlib import button
import time
prgmName = "pyshell"
prgmDesc = "python shell"
prgmAuthor = "system"
prgmVer = 0
prgmMinSysVer = 0.1
prgmIcon = ["1111111111111111",
            "1000000000000001",
            "1011110001010101",
            "1000000000000001",
            "1111111111111111",
            "1000000000000001",
            "1011111000000001",
            "1000000000000001",
            "1011100000000001",
            "1000000000000001",
            "1011110000000001",
            "1000000000000001",
            "1011000000000001",
            "1000000000000001",
            "1000000000000001",
            "1111111111111111"]
def main():
    gui.cli.auto = True
    toRun = gui.osk("command")
    if gui.ask("run with?","eval","exec"):
        try:
            temp = eval(str(toRun))
            gui.cli.printl("res: "+str(temp))
            gui.cli.printl("completed eval")
            gui.cli.printl("press A to quit")
            while not button.A.isPressed():
                pass
            return str(temp)
        except Exception as E:
            gui.cli.printl("FAILED")
            gui.cli.printl(str(E))
            gui.cli.printl("press A to quit")
            return "failed eval"
    else:
        try:
            exec(toRun)
            gui.cli.printl("completed exec")
            gui.cli.printl("press A to quit")
            return "ran"
        except Exception as E:
            gui.cli.printl("FAILED")
            gui.cli.printl(str(E))
            gui.cli.printl("press A to quit")
            return "failed exec"
