import time
from gfx_pack import GfxPack, SWITCH_A, SWITCH_B, SWITCH_C, SWITCH_D, SWITCH_E
gp = GfxPack()
display = gp.display
WIDTH, HEIGHT = display.get_bounds()
display.set_font("bitmap8")
lineTxt = []
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

def drawLine(x,y,x2,y2):
    display.set_pen(15)
    display.line(x,y,x2,y2)
    display.set_pen(0)
def drawImg(img, xpos = 8, ypos = 8, xsize = 8, ysize = 8):
    '''draws a image'''
    display.set_pen(15)
    for y in range(ysize):
        for x in range(xsize):
            if img[y][x]=="1":
                display.pixel(x+xpos,y+ypos)
    display.set_pen(0)
def printAt(text, x, y, size = 2):
    '''prints text at pos'''
    display.set_pen(15)
    display.text(text, x, y, WIDTH, size)
    display.set_pen(0)
class cli:
    auto = True
    def printl(text):
        text = str(text)
        '''prints text in cli'''
        def printInOrder():
            clear()
            for Txt in range(len(lineTxt)):
                display.text(str(lineTxt[Txt]), 0, Txt*8, 9999, 1)
            if cli.auto:
                update()
        if len(lineTxt)==8:
            del lineTxt[0]
        lineTxt.append(text)
        printInOrder()
    def clear():
        '''clears cli'''
        lineTxt = []
    def onDisp():
        '''get whats on display'''
        return lineTxt
def update():
    display.update()
def clear():
    '''clears the screen'''
    display.set_pen(0)
    display.clear()
    display.set_pen(15)
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
    
def osk(msg, oskString = "abcdefghijklmnopqrstuvwxyz0123456789!.,?*+-'\":()/\ " ,startstring = "" ):
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
def msgBox(msg, title = ""):
    '''displays a message box'''
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
            
        
