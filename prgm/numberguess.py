import os
import guilib as gui
import pputils as utils
from buttonlib import button
import time
import random
prgmName = "guess number"
prgmDesc = "guess to win the game"
prgmAuthor = "nova"
prgmVer = 0.1
prgmMinSysVer = 0.1
prgmIcon = ["1111111111111111",
            "1000000000000001",
            "1001001100110001",
            "1011000010001001",
            "1001000100110001",
            "1001001110001001",
            "1001000000110001",
            "1000000000000001",
            "1000000000000001",
            "1000000000000001",
            "1000000000000001",
            "1000000000000001",
            "1000000000000001",
            "1000000000000001",
            "1000000000000001",
            "1111111111111111"]
def main():
    running = True
    custom = False
    while running:
        chosen = gui.menu("number guess", "start guessing", "help","customize", "exit")
        if chosen == 1:
            if custom:
                game(minimum, maximum)
            else:
                game()
        elif chosen == 2:
            gui.splash("A game where you try to guess correct")
        elif chosen == 3:
            numberlol = 1
            while numberlol:
                custom = True
                gui.msgBox("whats the minimum number?")
                minimum = gui.osk("minimum number is ","0123456789")
                gui.msgBox("okay now for the max number?")
                maximum = gui.osk("maximum number is","0123456789")
                if minimum > maximum:
                    gui.msgBox("minimum cant be bigger then maximum")
                    pass
                elif minimum==maximum:
                    gui.msgBox("maximum and minimum cant be the same")
                numberlol = 0
        elif chosen == 4:
            if gui.ask("are you sure you want to quit?"):
                gui.msgBox("Goodbye!")
                running = False


def game(customMin = 0, customMax = 0):
    trys = 0
    if customMin == 0 and customMax == 0:
        minimum = 1
        maximum = random.randint(minimum,minimum+15)
    else:
        minimum = customMin
        maximum = customMax
    picked = random.randint(minimum,maximum)
    while 1:
        trys += 1
        userpicked = gui.osk("pick a number from "+str(minimum)+" to "+str(maximum),"0123456789")
        if int(userpicked) == picked:
            gui.msgBox("You win! with "+str(trys)+" trys")
            return 0
        if int(userpicked) > picked:
            gui.msgBox("number is smaller")
        elif picked > int(userpicked):
            gui.msgBox("number is bigger")