import time
import os
from dispobj import display, gp, WIDTH, HEIGHT, SWITCH_A, SWITCH_B, SWITCH_C, SWITCH_D, SWITCH_E
class backlight:
    def rgb(r=0,g=0,b=0):
        gp.set_backlight(r, g, b)
    def bright(blight = 1.0):
        gp.set_backlight(blight)
class img:
    boxcwar = ["11111",
               "10001",
               "10101",
               "10101",
               "10001",
               "10101",
               "10001",
               "11111"]
    emotiSmile8x8 = ["01111110",
                     "10000001",
                     "10100101",
                     "10000001",
                     "10100101",
                     "10011001",
                     "10000001",
                     "01111110"]        
def drawPixel(x,y):
    display.set_pen(15)
    display.pixel(x,y)
    display.set_pen(0)
def drawLine(x,y,x2,y2):
    display.set_pen(15)
    display.line(x,y,x2,y2)
    display.set_pen(0)
def drawBImg(img_data, xpos=8, ypos=8, xsize=8, ysize=8, startx=0, starty=0):
    '''draws an image using byte array'''
    display.set_pen(15)
    for y in range(ysize):
        for x in range(xsize):
            pixel_index = y * xsize + x
            if pixel_index < len(img_data) and img_data[pixel_index] == 1:
                display.pixel(startx + x + xpos, starty + y + ypos)
    display.set_pen(0)
def pimgOpen(link):
    with open(link,"r") as f: 
        data = f.read()
        data = data.split("$")
        if data[0] != "PIMG":
            return 8,8,bytearray([1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1])
        img_bytearray = eval(data[3])
        return int(data[1]),int(data[2]),img_bytearray

def drawImg(img, xpos = 8, ypos = 8, xsize = 8, ysize = 8, startx = 0, starty = 0):
    '''draws an image'''
    display.set_pen(15)
    for y in range(ysize):
        for x in range(xsize):
            try:
                if img[y][x]=="1":
                    display.pixel(startx+x+xpos,starty+y+ypos)
            except:
                    display.pixel(startx+x+xpos,starty+y+ypos)
    display.set_pen(0)
def printAt(text, x, y, size = 2):
    '''prints text at pos'''
    display.set_pen(15)
    display.text(text, x, y, WIDTH, size)
    display.set_pen(0)
def update():
    display.update()
def clear(update = False):
    '''clears the screen'''
    display.set_pen(0)
    display.clear()
    display.set_pen(15)
    if update:
        display.update()
def splash(msg, fontsize = 2):
    '''displays text in a splash screen'''
    clear()
    display.set_pen(15)
    display.text(msg, 0, 0, WIDTH, fontsize)
    display.text("press A", 0,56,WIDTH, 1)
    display.line(0,54,WIDTH,54)
    display.line(34,54,34,HEIGHT)
    display.update()
    while True:
            if gp.switch_pressed(SWITCH_A):
                while gp.switch_pressed(SWITCH_A):
                    time.sleep(0)
                return True
                
            time.sleep(0.1)
    clear()
    display.update()
def osk(msg, oskString = "abcdefghijklmnopqrstuvwxyz0123456789!.,?*+-'\":()/\ " ,startstring = ""):
    '''onscreen keyboard'''
    writenString = startstring
    print(oskString[len(oskString)-1])
    onKeyboard = True
    selected = 1
    while onKeyboard:
        if selected==len(oskString):
            selected = 0
        elif selected==-1:
            selected = len(oskString)-1
        clear()
        display.set_pen(15)
        display.text(msg, 0, 0, WIDTH, 1)
        display.text("-> "+oskString[selected], 0, 8, WIDTH, 1)
        display.text(writenString, 0,16, WIDTH, 1)
        display.update()
        time.sleep(0.1)
        if gp.switch_pressed(SWITCH_A):
            while gp.switch_pressed(SWITCH_A):
                pass
            selected -= 1
        elif gp.switch_pressed(SWITCH_B):
            while gp.switch_pressed(SWITCH_B):
                pass
            selected += 1
        elif gp.switch_pressed(SWITCH_C):
            while gp.switch_pressed(SWITCH_C):
                pass
            writenString += oskString[selected]
        elif gp.switch_pressed(SWITCH_D):
            while gp.switch_pressed(SWITCH_D):
                pass
            writenString = writenString[:-1]
        elif gp.switch_pressed(SWITCH_E):
            return writenString
                
    return oskString[0]
def ask(msg, custA = "Yes", custB = "No", fontsize = 1):
    '''asks for a question'''
    clear()
    display.set_pen(15)
    display.text(msg, 0, 0, WIDTH, fontsize)
    display.text("A. "+custA, 0,48,WIDTH, 1)
    display.text("B. "+custB, 0,56,WIDTH, 1)
    display.line(0,46,WIDTH,46)
    if len(custA) >= len(custB):
        display.line(len(custA)*5+15,46,len(custA)*5+15,HEIGHT)
    else:
        display.line(len(custB)*5+15,46,len(custB)*5+15,HEIGHT)
    display.update()
    time.sleep(1)
    print(msg)
    while gp.switch_pressed(SWITCH_A) or gp.switch_pressed(SWITCH_B):
        pass
    while True:
            if gp.switch_pressed(SWITCH_A):
                while gp.switch_pressed(SWITCH_A):
                    time.sleep(0)
                print(custA)
                return True
            elif gp.switch_pressed(SWITCH_B):
                while gp.switch_pressed(SWITCH_B):
                    time.sleep(0)
                print(custB)
                return False
                
            time.sleep(0.1)
    clear()
    display.update()
def menu(msg, custA = "None_", custB = "None_", custC = "None_", custD = "None_", custE = "None_",fontsize = 1, submsg = ""):
    '''displays a menu'''
    clear()
    display.set_pen(15)
    display.text(msg, 0, 0, WIDTH, fontsize)
    if custA != "None_":
        display.text("A. "+custA, 0,16,WIDTH, 1)
    if custB != "None_":
        display.text("B. "+custB, 0,24,WIDTH, 1)
    if custC != "None_":
        display.text("C. "+custC, 0,32,WIDTH, 1)
    if custD != "None_":
        display.text("D. "+custD, 0,40,WIDTH, 1)
    if custE != "None_":
        display.text("E. "+custE, 0,48,WIDTH, 1)
    display.text(submsg, 0,56,WIDTH, 1)
    display.update()
    time.sleep(1)
    print(msg)
    while gp.switch_pressed(SWITCH_A) or gp.switch_pressed(SWITCH_B) or gp.switch_pressed(SWITCH_C) or gp.switch_pressed(SWITCH_D) or gp.switch_pressed(SWITCH_E):
        pass
    while True:
            if gp.switch_pressed(SWITCH_A):
                if custA != "None_":
                    while gp.switch_pressed(SWITCH_A):
                        time.sleep(0)
                    print(custA)
                    return 1
            elif gp.switch_pressed(SWITCH_B):
                if custB != "None_":
                    while gp.switch_pressed(SWITCH_B):
                        time.sleep(0)
                    print(custB)
                    return 2
            elif gp.switch_pressed(SWITCH_C):
                if custC != "None_":
                    while gp.switch_pressed(SWITCH_C):
                        time.sleep(0)
                    print(custC)
                    return 3
                if custD != "None_":
                    while gp.switch_pressed(SWITCH_D):
                        time.sleep(0)
                    print(custD)
                    return 4
            elif gp.switch_pressed(SWITCH_E):
                if custE != "None_":
                    while gp.switch_pressed(SWITCH_E):
                        time.sleep(0)
                    print(custE)
                    return 5
                
            time.sleep(0.1)
    clear()
    display.update()
def msgBox(msg, title = "", wthC = True):
    '''displays a message box'''
    if wthC:
        clear()
    while gp.switch_pressed(SWITCH_A):
        pass
    Atime = 0
    Apos = 0
    display.set_pen(15) 
    display.line(16,16,104,16)
    display.line(16,16,16,48)
    display.line(104,16,104,48)
    display.line(16,48,104,48)
    display.line(90,38,104,38)
    display.line(90,38,90,48)
    if title == "":
        display.text(msg, 18,18,88, 1)
    else:
        display.line(16,28,104,28)
        display.text(msg, 26,26,88, 1)
    while 1:
        display.set_pen(0)
        for i in range(98):
            display.line(16,i+16,104,1+16)
        display.set_pen(15)
        display.line(16,16,104,16)
        display.line(16,16,16,48)
        display.line(104,16,104,48)
        display.line(16,48,104,48)
        display.line(90,38,104,38)
        display.line(90,38,90,48)
        if Apos==0:
            display.set_pen(0)
            display.text("A", 94,40,WIDTH, 1)
            display.set_pen(15)
            display.text("A", 96,40,WIDTH, 1)
        else:
            display.set_pen(0)
            display.text("A", 96,40,WIDTH, 1)
            display.set_pen(15)
            display.text("A", 94,40,WIDTH, 1)
        display.text(msg, 18,18,88, 1)
        display.update()
        time.sleep(0.1)
        Atime += 2
        if Atime==10:
            if Apos==1:
                Apos = 0
            elif Apos==0:
                Apos = 1
            Atime = 0
        if gp.switch_pressed(SWITCH_A):
                while gp.switch_pressed(SWITCH_A):
                    pass
                clear()
                display.update()
                time.sleep(0.5)
                return 1
def file(reason,location = "/", canfolder = False):
    def strinsert (source_str, insert_str, pos):
        return source_str[:pos] + insert_str + source_str[pos:]
    def dir_exists(filename):
        try:
            return (os.stat(filename)[0] & 0x4000) != 0
        except OSError:
            return False
    flocation = location
    files = os.listdir(location)
    if flocation != "/":
        files.insert(0,"..")
    selection = 0
    while 1:
        if gp.switch_pressed(SWITCH_A):
            while gp.switch_pressed(SWITCH_A):
                pass
            selection -= 1
        elif gp.switch_pressed(SWITCH_B):
            while gp.switch_pressed(SWITCH_B):
                pass
            selection += 1
        elif gp.switch_pressed(SWITCH_E):
            while gp.switch_pressed(SWITCH_E):
                pass
            splash(flocation+"/"+files[selection],1)
            if not canfolder:
                if dir_exists(flocation+"/"+files[selection]):
                    if files[selection] == "..":
                        temp = flocation.split("/")
                        del temp[-1]
                        flocation = "/".join(temp)
                        if flocation[0] != "/":
                            strinsert(flocation,"/",0)
                    else:
                        flocation = flocation+"/"+files[selection]
                    files = os.listdir(flocation)
                    if flocation != "/":
                        files.insert(0,"..")
                    selection = 0
                else:
                    return flocation+"/"+files[selection]
            else:
                return flocation+"/"+files[selection]
        if selection == -2:
            selection = len(files)-1
        elif selection == len(files):
            selection = 0
        clear()
        display.text(reason,0,0,999999,1)
        showselect = True
        if showselect:
            if dir_exists(location+"/"+str(selection)):
                display.text("selected directory:",0,16,WIDTH,1)
            else:
                display.text("selected file:",0,16,WIDTH,1)
            display.text(files[selection],0,24,WIDTH,1)
            display.update()