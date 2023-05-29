import guilib as gui
import time
from buttonlib import button
prgmName = "presentation"
prgmDesc = "presentation application"
prgmAuthor = "test"
prgmMinSysVer = 0.2
prgmVer = 0
prgmIcon = ["1111111100000000","1111111100000000","1111111100000000","1111111100000000","1111111100000000","1111111100000000","1111111100000000","1111111100000000","0000000011111111","0000000011111111","0000000011111111","0000000011111111","0000000011111111","0000000011111111","0000000011111111","0000000011111111"]
def hsv_to_rgb(h, s, v):
    if s == 0.0:
        return v, v, v
    i = int(h * 6.0)
    f = (h * 6.0) - i
    p = v * (1.0 - s)
    q = v * (1.0 - s * f)
    t = v * (1.0 - s * (1.0 - f))
    i = i % 6
    if i == 0:
        return v, t, p
    if i == 1:
        return q, v, p
    if i == 2:
        return p, v, t
    if i == 3:
        return p, q, v
    if i == 4:
        return t, p, v
    if i == 5:
        return v, p, q
    if button.A.ispressed():
        return
def techdemo(op):
    h = 0
    if op == 1:
        speedx = 1
        speedy = 1
        x = 0
        y = 0
        while 1:
            x += speedx
            y += speedy
            gui.clear()
            gui.printAt("Colours!",x,y)
            gui.update()
            h += 1
            r, g, b = [int(255 * c) for c in hsv_to_rgb(h / 360.0, 1.0, 1.0)]  # rainbow magic
            gui.backlight.rgb(r,g,b)
            time.sleep(1.0 / 60)
            if y == 0:
                speedy = 1
            elif y == 48:
                speedy = -1
            if x == 56:
                speedx = -1
            elif x == 0:
                speedx = 1
            if button.A.isPressed():
                return 0
    elif op ==2:
        window1 = gui.window("window 1")
        window2 = gui.window("window 2",True)
        quitWindow = gui.window("Do you want to exit?",True)
        text1 = gui.window.label("this is window 1!",0,16)
        text1_1 = gui.window.label("Press A!",0,24)
        text2 = gui.window.label("this window has an icon!",0,16)
        quitText = gui.window.label("Press A to confirm",0,16)
        quitText2 = gui.window.label("Press B to not",0,24)
        selected = 1
        count = 0
        while 1:
            if button.D.isPressed():
                gui.clear()
                quitText.draw()
                quitText2.draw()
                quitWindow.draw()
                looping = True
                while looping:
                    if button.A.isPressed():
                        return
                    elif button.B.isPressed():
                        looping = False
            gui.clear()
            if selected == 1:
                text1.draw()
                if button.A.isPressed():
                    count += 1
                    text1_1.contents = "button A pressed: "+str(count)
                text1_1.draw()
                window1.draw()
            elif selected == 2:
                text2.draw()
                window2.draw()
            if button.E.isPressed():
                if selected == 1:
                   selected = 2
                elif selected == 2:
                    selected = 1   
def main():
    running = True
    while running:
        option = gui.menu("presentation","rgb tech demo","app interface","exit")
        if option != 3:
            techdemo(option)
        else:
            running = False