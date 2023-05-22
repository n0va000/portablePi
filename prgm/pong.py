import random
import machine
import guilib as gui
import pputils as utils
from buttonlib import button
import time
import math as m
prgmName = "pong"
prgmDesc = "simple pong game"
prgmAuthor = "nova"
prgmVer = 0.1
prgmMinSysVer = 0.2
prgmIcon = ["1111111111111111",
            "1000000000000001",
            "1000000000000001",
            "1000000000000001",
            "1000000000000001",
            "1000000000000001",
            "1000000000000001",
            "1000000000000001",
            "1000000000000001",
            "1000000000000001",
            "1000000000010001",
            "1000000000000001",
            "1000000000000001",
            "1001111111100001",
            "1000000000000001",
            "1111111111111111"]
    
def main():
    running = True
    while running:
        chosen = gui.menu("Welcome to pong!","start game","help", "quit")
        if chosen == 1:
            game()
        elif chosen == 2:
            gui.splash("A game where you try to bounce a ball")
        elif chosen == 3:
            if gui.ask("Really want to quit?"):
                gui.msgBox("Goodbye!")
                running = False
        
def game():
    score = 0
    machine.freq(249000000)
    gui.msgBox("Good luck")
    wall = ["10000000",
            "00000000",
            "00100100",
            "00000000",
            "00010001",
            "00000100",
            "00101000",
            "00000001"]
    wall = wall*8
    ballimg = ["00111100",
               "01111110",
               "11111111",
               "11111111",
               "11111111",
               "11111111",
               "01111110",
               "00111100"]
    paddlex = 32
    if random.randint(0,1):
        ballx = 34
        bally = 32
    else:
        ballx = 84
        bally = 16
    ballspeedx = getXspeed()
    ballspeedy = getYspeed()
    EasyMode = gui.ask("what mode?","easy", "hard")
    while True: # main loop
        gui.clear()
        ballx += ballspeedx
        bally += ballspeedy
        gui.drawLine(paddlex,60,paddlex+16,60)
        gui.drawImg(ballimg, int(ballx),int(bally))
        for secondi in range(4):
            gui.drawImg(wall, secondi*8, 0,8,48)
            gui.drawImg(wall, 120-secondi*8, 0,8,48)
        gui.printAt(str(score),34,0)
        gui.printAt("Pong!",0,48,1)
        gui.printAt("Pong!",0,56,1)
        gui.printAt("Pong!",96,48,1)
        gui.printAt("Pong!",96,56,1)
        gui.drawLine(32,0,32,gui.HEIGHT)
        gui.drawLine(96,0,96,gui.HEIGHT)
        if button.A.isDown():
            if paddlex != 32:
                paddlex -= 2
        elif button.B.isDown():
            if paddlex != 80:
                paddlex += 2
        if ballx == 88:
            if random.randint(1,3)==3:
                ballspeedy = 1
            ballspeedx = -1
        elif 32 == ballx:
            if random.randint(1,3)==3:
                ballspeedy = 1
            ballspeedx = 1
        if 0 > bally:
            ballspeedy = 1
        if bally == 52: # col detect
                print(str(ballx)+" "+str(paddlex))
                if ballx+8 > paddlex and paddlex+16 > ballx:
                    print(0)
                    ballspeedy = -1
                    ballspeedx = -1
                    score += 1
                elif ballx>paddlex:
                     pass
                elif ballx+8 > paddlex+8 and paddlex+10>ballx+8 :
                    print(1)
                    ballspeedy = -1
                    ballspeedx = 1
                    score += 1
        elif bally > 60:
            gui.msgBox("You lost! score: "+str(score))
            return
        if EasyMode:
            time.sleep(0.05)
        gui.update()
def getXspeed():
    if random.randint(0,1):
        return 1
    else:
        return -1
def getYspeed():
    if random.randint(0,1):
        return 1
    else:
        return -1
    
